# Copyright (c) 2010-2021 openpyxl

from sfg.openpyxl.descriptors import (
    Bool,
    String,
    Typed
)
from sfg.openpyxl.descriptors import Serialisable
from openpyxl.styles import Color


class ChartsheetProperties(Serialisable):
    tagname = "sheetPr"

    published = Bool(allow_none=True)
    codeName = String(allow_none=True)
    tabColor = Typed(expected_type=Color, allow_none=True)

    __elements__ = ('tabColor',)

    def __init__(self,
                 published=None,
                 codeName=None,
                 tabColor=None,
                 ):
        self.published = published
        self.codeName = codeName
        self.tabColor = tabColor
