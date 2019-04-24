# Smack 💬
SMS-based chat room, similar-ish to Slack. There's a built-in invite system, muting/unmuting, and it's easily extendable. Have at it!

# Usage 💬
* `#join <nickname>`: Join the chat and set your nickname (20 letter maximum)
* `#update <new nickname>`: Update your nickname (20 letter maximum)
* `#invite <phone number>`: Invite a new user via SMS to the phone number provided
* `#who <nickname>`: Get information about a user by providing their nickname if the profile is set to public. Default is private
* `#private <on|off>`: Make your profile public or private. Default is private
* `#stop`: Stop receiving messages from this Smack room
* `#start`: Start receiving message from this Smack room
* `#list`: List all users in the room
* `#resend <number>`: Resend the previous \<number> of messages sent to you
* `#mute <nickname> <on|off>`: Stop or start receiving messages from this user
* `#help`: List help for all commands
* `#help <command>`: List help for command specified

# Requirements 💬
* Publicly addressable machine/VPS/ngrok instance/etc.
* Python 3.7.2
* Redis server installed
 * `brew install redis-server` and follow the instructions to get it to start on boot
* Neo4j installed for social graph
 * I'm using homebrew, so it was `brew install neo4j`, which also depended on installing Java8: `brew cask install homebrew/cask-versions/java8`
 
## Twilio 💬
* This app requires a Twilio account, setup to post to whatever IP/port you've exposed on the server

## Neo4J 💬
* Using the neomodel python library for now since it seems to provide a nice modeling abstraction. Might need to use the official driver for other stuff, so it's installed for now but will be removed if not used.

## Redis Queue (rq) 💬
* `rq worker` will process whatever is currently in the queue
* `rq info <default|failed>` will give information about what's currently in the queue
* `rq empty <default|failed>` will clear the specified queue

## Honcho 💬
* honcho start will start all your services

## User/Phone Data Model 💬
* Number: User's phone number, string, length=10 (US Only), 25 (Int'l)
 * Can't be integer because many phone numbers start with 0 (due to country codes)
 * Second pass will be to abstract out country code and phone number
* Owner: ForeignKey to Flask's User/Auth model if possible
* Muted_by: Many to Many with User
* get\_reply\_numbers: Function that returns all phone numbers, excluding your own, excluding any that you have been muted by, and excluding any that are is_active = False
* is_active: Bool default True
* is_private: Bool default True

## Data available from Twilio 💬
 * 'ToCountry', 'US'
 * 'ToState', 'CA'
 * 'SmsMessageSid', 'SMb7f1146ce509ee2bc7af12e14ac91143
 * 'NumMedia', '0'
 * 'ToCity', 'MILL VALLEY'
 * 'FromZip', ''
 * 'SmsSid', 'SMb7f1146ce509ee2bc7af12e14ac91143'
 * 'FromState', 'CA'
 * 'SmsStatus', 'received'
 * 'FromCity', ''
 * 'Body', '#test'
 * 'FromCountry', 'US'
 * 'To', '+14158776225'
 * 'ToZip', '94941'
 * 'NumSegments', '1'
 * 'MessageSid', 'SMb7f1146ce509ee2bc7af12e14ac91143'
 * 'AccountSid', 'ACdd5eac9075d080bd7c50819cbf25b64b'
 * 'From', '+15107755852'
 * 'ApiVersion', '2010-04-01'
