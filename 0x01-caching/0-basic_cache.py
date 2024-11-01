#!/usr/bin/env python3
"""
This is Basic ditionary
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    This Basic Cache class inherits from BaseCaching
    """

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
