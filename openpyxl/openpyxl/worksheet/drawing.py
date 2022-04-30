# Copyright (c) 2010-2021 openpyxl

from sfg.openpyxl.descriptors import Serialisable
from sfg.openpyxl.descriptors import Relation


class Drawing(Serialisable):

    tagname = "drawing"

    id = Relation()

    def __init__(self, id=None):
        self.id = id
