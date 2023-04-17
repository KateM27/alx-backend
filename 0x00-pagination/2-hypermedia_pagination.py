#!/usr/bin/env python3
'''Hypermedia pagination'''

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''Return a tuple of size two with a start index
    corresponding to the range of indexes to return in
    a list for those particular pagination parameters'''
    myTuple = page_size * (page - 1), page * page_size
    return myTuple


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
        '''simple pagination'''
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        indxs = index_range(page, page_size)
        try:
            data = self.dataset()
            return data[indxs[0]: indxs[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''return a dictionary with some key/value pairs'''
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
              "page_size": len(data),
              "page": page,
              "data": data,
              "next_page": next_page,
              "prev_page": prev_page,
              "total_pages": total_pages
         }
