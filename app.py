#!/usr/bin/env python

from flask import Flask, request, redirect
from redis import Redis
from rq import Queue
from twilio.twiml.messaging_response import MessagingResponse
from smack.commands import Commands

import logging

COMMAND_IDENTIFIER = "#"

app = Flask(__name__)

c = Commands()
q = Queue(connection=Redis())

def parse(req):
    from_n = req.form['from']
    body = req.form['body']

    body_parts = body.split()
    if body.startswith(COMMAND_IDENTIFIER):
        command = body_parts[0].lstrip('#').lower()
    else:
        command = None

    return (from_n, body, body_parts, command)

@app.route("/", methods=['GET'])
def index():
    return ("Commands are: %s%s" % (COMMAND_IDENTIFIER, ", #".join(combined.keys())), 200)

@app.route("/sync", methods=['POST'])
def process_sync():
    """Respond to incoming sms with a simple text message"""

    # Start the TwiML response
    resp = MessagingResponse()

    # Add message to response
    resp.message("This is a default message for synchronous sms.")

    return str(resp)

@app.route("/async", methods=['POST'])
def process_async():
    from_n, body, body_parts, command = parse(request)
    q.enqueue(c.combined[command], from_n, body, body_parts)
    logging.info("Enqueued: %s" % command)

    return ('', 204)

if __name__ == "__main__":
    app.run(debug=True)
