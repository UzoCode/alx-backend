#!/usr/bin/env python3
"""Function that defines stellar function"""
from typing import Optional, Mapping, Tuple


def index_range(*args: Optional[Tuple[int]],
                **kwargs: Optional[Mapping[str, int]]) -> Tuple:
    """Function takes two integer arguments

    Params:
    page():
    page_size()

    Returns:
        Tuple of size=2 that contains `start index` and `end index`
        corresponding to range of indexes returned in list
        for those particular pagination parameters.

        Note:
           The page numbers are 1-indexed, (the first page is page 1).
    """
    if len(args) == 2:
        page, page_size = args
    elif len(kwargs) == 2:
        page = kwargs.get('page')
        page_size = kwargs.get('page_size')
    else:
        return ()
    end = page * page_size
    return (end - page_size, end)
