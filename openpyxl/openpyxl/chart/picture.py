# Copyright (c) 2010-2021 openpyxl

from sfg.openpyxl.descriptors import Serialisable

from sfg.openpyxl.descriptors import (
    NestedBool,
    NestedFloat,
    NestedMinMax,
    NestedNoneSet,
)

class PictureOptions(Serialisable):

    tagname = "pictureOptions"

    applyToFront = NestedBool(allow_none=True, nested=True)
    applyToSides = NestedBool(allow_none=True, nested=True)
    applyToEnd = NestedBool(allow_none=True, nested=True)
    pictureFormat = NestedNoneSet(values=(['stretch', 'stack', 'stackScale']), nested=True)
    pictureStackUnit = NestedFloat(allow_none=True, nested=True)

    __elements__ = ('applyToFront', 'applyToSides', 'applyToEnd', 'pictureFormat', 'pictureStackUnit')

    def __init__(self,
                 applyToFront=None,
                 applyToSides=None,
                 applyToEnd=None,
                 pictureFormat=None,
                 pictureStackUnit=None,
                ):
        self.applyToFront = applyToFront
        self.applyToSides = applyToSides
        self.applyToEnd = applyToEnd
        self.pictureFormat = pictureFormat
        self.pictureStackUnit = pictureStackUnit
