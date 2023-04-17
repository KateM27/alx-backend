#!/usr/bin/env python3
'''Creating a simple helper function'''


def index_range(page: int, page_size: int) -> tuple:
    '''Return a tuple of size two with a start index
    corresponding to the range of indexes to return in
    a list for those particular pagination parameters'''
    myTuple = page_size * (page - 1), page * page_size
    return myTuple
