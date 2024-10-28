#!/usr/bin/env python3
"""
This is Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Optional


class Server:
    """Server class paginates database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """The Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Indexed Dataset by sorting position, starts at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """To enforce data integrity after deletes

        Params:
           index(int): current start index of return page.
            Meaning, the index of first item in current page.
           next_incex(int): next index to query with. This is
            index of first item after last item on current page.
           page_size(int): current page size
           data(obj:list[list[str]]): actual page of the dataset

        Requirements/Behavior:
          (1). Assert verifies that index is in valid range.
          (2). When user queries index 0, page_size 10,
               rows indexed 0 to 9 will be included.
          (3). If the next index (10) with page_size 10, is requested
               but rows 3, 6 and 7 were deleted, user should
               receive rows indexed 10 to 19 included.
        """
        assert isinstance(index, int) and index >= 0 \
            and index < len(self.__indexed_dataset)
        assert isinstance(page_size, int) and page_size > 0 \
            and page_size < len(self.__indexed_dataset)
        result = []
        next_idx = None
        current_idx = index
        items = 0
        while True:
            if items == page_size:
                break
            data = self.__indexed_dataset.get(current_idx)
            next_idx = current_idx + 1
            if data:
                result.append(data)
                items += 1
            current_idx = next_idx
        return {
            "index": index,
            "next_index": next_idx,
            "page_size": page_size,
            "data": result
        }
