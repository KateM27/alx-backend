#!/usr/bin/env python3
"""LRU caching"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """class inherits from BaseCaching"""
    def __init__(self):
        """Initialize class instance"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add key/value pair to the cache"""
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.keys:
                rem_key = self.keys.pop(0)
                del self.cache_data[rem_key]
                print("DISCARD: {}".format(rem_key))
            if key in self.keys:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Return the value of key in cache"""
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        value = self.cache_data.get(key)
        return value
