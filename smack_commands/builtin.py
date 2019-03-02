def cmd_help(*args, **kwargs): lambda: None
def cmd_invite(*args, **kwargs): lambda: None
def cmd_join(*args, **kwargs): lambda: None
def cmd_list(*args, **kwargs): lambda: None
def cmd_mute(*args, **kwargs): lambda: None
def cmd_private(*args, **kwargs): lambda: None
def cmd_resend(*args, **kwargs): lambda: None
def cmd_start(*args, **kwargs): lambda: None
def cmd_stop(*args, **kwargs): lambda: None
def cmd_start(*args, **kwargs): lambda: None
def cmd_update(*args, **kwargs): lambda: None
def cmd_who(*args, **kwargs): lambda: None

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
