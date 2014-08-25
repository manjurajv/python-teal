# -*- coding: utf-8 -*-
""" teal.lib.Transporter """


class TransporterError(Exception):
    def __init__(self, code, msg):
        super(TransporterError, self).__init__(code, msg)
        self.code = code
        self.msg = msg

    def __str__(self):
        return "(%s): %s" % (self.code, self.msg)
