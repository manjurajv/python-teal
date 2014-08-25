# -*- coding: utf-8 -*-
""" teal.lib.Transporter """
from subprocess import check_call, check_output
from error import TransporterError
from base import TransporterBase


class TransporterNative(TransporterBase):
    def __init__(self, **kwargs):
        super(TransporterNative, self).__init__(**kwargs)

    @classmethod
    def is_transporter_for(cls, trans_name):
        if trans_name == 'Native':
            return True
        return False

    def get_smaps(self, pid):
        try:
            smaps = check_output(["cat", "/proc/" + str(pid) + "/smaps"])
            return smaps
        except:
            raise TransporterError(422, "Unable to fetch smaps")

    def get_pids(self):
        try:
            pids = [int(pid) for pid in os.listdir("/proc") if pid.isdigit()]
            return pids
        except:
            raise TransporterError(423, "Unable to fetch PIDs")

    def get_status(self, pid):
        try:
            status = check_output(["cat", "/proc/" + str(pid) + "/status"])
            return status
        except:
            raise TransporterError(424, "Unable to fetch status")

    def get_version(self):
        try:
            version = check_output(["cat", "/proc/version"])
            return version
        except:
            raise TransporterError(425, "Unable to fetch version")
