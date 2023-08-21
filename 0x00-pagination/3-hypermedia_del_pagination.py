#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

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

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """A method that takes two integer arguments page with default value 1
        and page_size with default value 10."""
        assert type(index) == int
        assert type(page_size) == int
        assert 0 <= index < len(self.__indexed_dataset)
        indexed_dataset = self.indexed_dataset()
        data = []
        next_index = index + page_size
        for i in range(index, next_index):
            if indexed_dataset.get(i):
                data.append(indexed_dataset[i])
            else:
                next_index += 1
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
