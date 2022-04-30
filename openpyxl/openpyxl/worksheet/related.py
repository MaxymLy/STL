# Copyright (c) 2010-2021 openpyxl

from sfg.openpyxl.descriptors import Serialisable
from sfg.openpyxl.descriptors import Relation


class Related(Serialisable):

    id = Relation()


    def __init__(self, id=None):
        self.id = id


    def to_tree(self, tagname, idx=None):
        return super(Related, self).to_tree(tagname)
