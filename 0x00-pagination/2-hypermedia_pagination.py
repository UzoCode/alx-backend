#!/usr/bin/env python3
"""Defining a Server class and utility functions"""

import csv
import math
from typing import List, Mapping, Optional, Tuple


def index_range(*args, **kwargs) -> Tuple:
    """This function takes two integer arguments

    Params:
    args(obj:tuple[int]): normally passed args,which are ints
    kwargs(obj:dict[str, int]): keyword arguments dictionary

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


class Server:
    """A Server class paginating database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """The Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Mapping:
        """Implementing Hypermedia pagination
        """
        dataset = self.get_page(page, page_size)
        total_size = len(self.__dataset)
        total_pages = total_size // page_size \
            if not total_size % page \
            else (total_size // page_size) + 1
        return {
            "page_size": len(dataset),
            "page": page,
            "data": dataset,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Fetches particular page data based on page_size
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        indexes: Tuple = index_range(page=page, page_size=page_size)
        dataset = self.__dataset or self.dataset()
        return dataset[indexes[0]: indexes[1]]
