from twilio.rest import Client
from .worker import Worker

from . import config
import os

class Message:

    def __init__(self):
        self.account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        self.auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        self.twilio_number = os.environ.get('TWILIO_NUMBER')

    def parse(self, request):
        from_n = request.form['From']
        body = request.form['Body']

        body_parts = body.split()
        if body.startswith(config.COMMAND_IDENTIFIER):
            command = body_parts[0].lstrip(config.COMMAND_IDENTIFIER).lower()
        else:
            command = None

        return (from_n, body, body_parts, command)

    def send(self, to, body):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
                body = body,
                from_= self.twilio_number,
                to = to
                )

        return message.sid
