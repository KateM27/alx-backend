#!/usr/bin/env python3
"""Basic caching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class inherits from BaseCaching"""
    def put(self, key, item):
        """Assign a key/value pair to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value of key in cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None

# my_cache = BasicCache()
# my_cache.print_cache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.print_cache()
# print(my_cache.get("A"))
# print(my_cache.get("B"))
# print(my_cache.get("C"))
# print(my_cache.get("D"))
# my_cache.print_cache()
# my_cache.put("D", "School")
# my_cache.put("E", "Battery")
# my_cache.put("A", "Street")
# my_cache.print_cache()
# print(my_cache.get("A"))
