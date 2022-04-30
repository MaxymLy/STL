# Copyright (c) 2010-2021 openpyxl

from sfg.openpyxl.descriptors import Bool
from sfg.openpyxl.descriptors import Serialisable


class Protection(Serialisable):
    """Protection options for use in styles."""

    tagname = "protection"

    locked = Bool()
    hidden = Bool()

    def __init__(self, locked=True, hidden=False):
        self.locked = locked
        self.hidden = hidden
