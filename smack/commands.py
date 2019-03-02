class Commands:

    def __init__(self):

        self.builtin = {
            'help': self.cmd_help,
            'invite': self.cmd_invite,
            'join': self.cmd_join,
            'list': self.cmd_list,
            'mute': self.cmd_mute,
            'private': self.cmd_private,
            'resend': self.cmd_resend,
            'start': self.cmd_start,
            'stop': self.cmd_stop,
            'update': self.cmd_update,
            'who': self.cmd_who
        }

        self.custom = {
            'test': self.cmd_test
        }

        self.combined = self.builtin.copy()
        self.combined.update(self.custom)

    @classmethod
    def cmd_help(self, from_n, body, body_parts):
            print "[BUILTIN] command: help"
            print "from_n: %s body: %s body_parts: %s" % (from_n, body, body_parts)

    @classmethod
    def cmd_invite(self, from_n, body, body_parts):
            print "[BUILTIN] command: invite"
            print "from_n: %s body: %s body_parts: %s" % (from_n, body, body_parts)

    @classmethod
    def cmd_join(self, from_n, body, body_parts):
            print "[BUILTIN] command: join"
            print "from_n: %s body: %s body_parts: %s" % (from_n, body, body_parts)

    @classmethod
    def cmd_list(self, from_n, body, body_parts):
            print "[BUILTIN] command: list"
            print "from_n: %s body: %s body_parts: %s" % (from_n, body, body_parts)

    @classmethod
    def cmd_mute(self, from_n, body, body_parts):
            print "[BUILTIN] command: mute"
            print "from_n: %s body: %s body_parts: %s" % (from_n, body, body_parts)

    @classmethod
    def cmd_private(self, from_n, body, body_parts):
            print "[BUILTIN] command: private"
            print "from_n: %s body: %s body_parts: %s" % (from_n, body, body_parts)

    @classmethod
    def cmd_resend(self, from_n, body, body_parts):
            print "[BUILTIN] command: resend"
            print "from_n: %s body: %s body_parts: %s" % (from_n, body, body_parts)

    @classmethod
    def cmd_start(self, from_n, body, body_parts):
            print "[BUILTIN] command: start"
            print "from_n: %s body: %s body_parts: %s" % (from_n, body, body_parts)

    @classmethod
    def cmd_stop(self, from_n, body, body_parts):
            print "[BUILTIN] command: stop"
            print "from_n: %s body: %s body_parts: %s" % (from_n, body, body_parts)

    @classmethod
    def cmd_start(self, from_n, body, body_parts):
            print "[BUILTIN] command: start"
            print "from_n: %s body: %s body_parts: %s" % (from_n, body, body_parts)

    @classmethod
    def cmd_update(self, from_n, body, body_parts):
            print "[BUILTIN] command: update"
            print "from_n: %s body: %s body_parts: %s" % (from_n, body, body_parts)

    @classmethod
    def cmd_who(self, from_n, body, body_parts):
            print "[BUILTIN] command: who"
            print "from_n: %s body: %s body_parts: %s" % (from_n, body, body_parts)

    @classmethod
    def cmd_test(self, from_n, body, body_parts):
            print "[CUSTOM] command: test"
            print "from_n: %s body: %s body_parts: %s" % (from_n, body, body_parts)
