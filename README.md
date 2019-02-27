# Smack
SMS-based chat room, similar-ish to Slack. There's a built-in invite system, muting/unmuting, and it's easily extendable. Future work will be done to move away from the current monolithic txt view to something more modular, using a dispatch pattern. Have at it!

# Usage
* `#join <nickname>`: Join the chat and set your nickname (20 letter maximum)
* `#update <new nickname>`: Update your nickname (20 letter maximum)
* `#invite <phone number>`: Invite a new user via SMS to the phone number provided
* `#who <nickname>`: Get information about a user by providing their nickname if the profile is set to public. Default is private
* `#private <on|off>`: Make your profile public or private. Default is private
* `#stop`: Stop receiving messages from this Smack room
* `#start`: Start receiving message from this Smack room
* `#list`: List all users in the room
* `#resend <number>`: Resend the previous <number> of messages sent to you
* `#mute <nickname> <on|off>`: Stop or start receiving messages from this user
* `#help`: List help for all commands
* `#help <command>`: List help for command specified

## Requirements
* Publicly addressable machine/VPS/etc.
* Python 2.7.10 or higher, has not been tested with Python 3.x 
 * No reason necessarily that this couldn't work with 3.x, but has not been tested.
  * PRs welcome!
* Filesystem access for the sqlite db or DB access - this is a Django app, so just change the settings.py accordingly
* Edit the settings.py-sample and rename to settings.py before starting
## Twilio
* This app requires a Twilio account, setup to post to whatever IP/port you've exposed on the server
