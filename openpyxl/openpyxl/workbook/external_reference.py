# Copyright (c) 2010-2021 openpyxl

from sfg.openpyxl.descriptors import Serialisable
from sfg.openpyxl.descriptors import (
    Sequence
)
from sfg.openpyxl.descriptors import (
    Relation,
)

class ExternalReference(Serialisable):

    tagname = "externalReference"

    id = Relation()

    def __init__(self, id):
        self.id = id
