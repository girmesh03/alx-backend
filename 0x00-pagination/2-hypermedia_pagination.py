#!/usr/bin/env python3
"""A module containing a function named get_hyper that takes two integer
arguments page with default value 1 and page_size with default value 10."""

import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of size two containing
    a start index and an end index."""
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """A method that takes two integer arguments page with default value 1
        and page_size with default value 10."""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        self.dataset()
        start, end = index_range(page, page_size)
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """A method that takes the same arguments (and defaults) as get_page
        and returns a dictionary containing the following key-value pairs."""
        total_pages = math.ceil(len(self.get_page()) / page_size)
        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
