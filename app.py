#!/usr/bin/env python

from flask import Flask, request, redirect
from redis import Redis
from rq import Queue
from twilio.twiml.messaging_response import MessagingResponse

import logging

COMMAND_IDENTIFIER = "#"

app = Flask(__name__)
q = Queue(connection=Redis())

def parse(req):
    from_n = request.form['From']
    body = request.form['Body']

    body_parts = body.split()
    if body.startswith(COMMAND_IDENTIFIER):
        command = body_parts[0].lower()
    else:
        command = None

    return (from_n, body, body_parts, command)

def join(): lambda: None
def start(): lambda: None

commands = {
    '%sjoin' % COMMAND_IDENTIFIER: join,
    '%sstart' % COMMAND_IDENTIFIER: start,
    }

@app.route("/ssms", methods=['GET','POST'])
def synch_sms_receive_with_reply():
    """Respond to incoming sms with a simple text message"""

    # Start the TwiML response
    resp = MessagingResponse()

    # Add message to response
    resp.message("This is a default message for synchronous sms.")

    return str(resp)

@app.route("/asms", methods=['POST'])
def async_sms_receive():
    q.enqueue(commands[command], from_n, body, body_parts)
    logging.info("Enqueued: %s" % command)

    return ('', 204)

if __name__ == "__main__":
    app.run(debug=True)
