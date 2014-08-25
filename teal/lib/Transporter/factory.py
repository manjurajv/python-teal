# -*- coding: utf-8 -*-
from error import TransporterError
from base import TransporterBase


def TransporterFactory(trans_name):
    for cls in TransporterBase.__subclasses__():
        if cls.is_transporter_for(trans_name):
            return cls(trans_name=trans_name)

    raise TransporterError(420, "Unable to find Transporter for " + trans_name)
