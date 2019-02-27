def cmd_help(): lambda: None
def cmd_invite(): lambda: None
def cmd_join(): lambda: None
def cmd_list(): lambda: None
def cmd_mute(): lambda: None
def cmd_private(): lambda: None
def cmd_resend(): lambda: None
def cmd_start(): lambda: None
def cmd_stop(): lambda: None
def cmd_start(): lambda: None
def cmd_update(): lambda: None
def cmd_who(): lambda: None

commands = {
    'help': cmd_help,
    'invite': cmd_invite,
    'join': cmd_join,
    'list': cmd_list,
    'mute': cmd_mute,
    'private': cmd_private,
    'resend': cmd_resend,
    'start': cmd_start,
    'stop': cmd_stop,
    'update': cmd_update,
    'who': cmd_who
}
