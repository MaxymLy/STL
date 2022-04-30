# Copyright (c) 2010-2021 openpyxl


from sfg.openpyxl.descriptors import Serialisable
from sfg.openpyxl.descriptors import (
    Sequence,
    Alias
)


class AuthorList(Serialisable):

    tagname = "authors"

    author = Sequence(expected_type=str)
    authors = Alias("author")

    def __init__(self,
                 author=(),
                ):
        self.author = author
