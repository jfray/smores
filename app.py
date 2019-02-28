#!/usr/bin/env python

from flask import Flask, request, redirect
from redis import Redis
from rq import Queue
from twilio.twiml.messaging_response import MessagingResponse
from commands import builtin, custom

import logging

COMMAND_IDENTIFIER = "#"

app = Flask(__name__)
q = Queue(connection=Redis())

combined = builtin.commands.copy()
combined.update(custom.commands)

def parse(req):
    from_n = request.form['From']
    body = request.form['Body']

    body_parts = body.split()
    if body.startswith(COMMAND_IDENTIFIER):
        command = body_parts[0].lower()
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
    q.enqueue(combined[command], from_n, body, body_parts)
    logging.info("Enqueued: %s" % command)

    return ('', 204)

if __name__ == "__main__":
    app.run(debug=True)
