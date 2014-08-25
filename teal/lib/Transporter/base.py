# -*- coding: utf-8 -*-
""" teal.lib.Transporter """
from abc import ABCMeta, abstractmethod


class TransporterBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, **kwargs):
        self.trans_name = kwargs.get('trans_name')

    @abstractmethod
    def is_transporter_for(cls, trans_name):
        raise NotImplementedError

    def get_smaps(self, pid):
        return NotImplementedError

    def get_pids(self):
        return NotImplementedError

    def get_status(self, pid):
        return NotImplementedError

    def get_version(self):
        return NotImplementedError
