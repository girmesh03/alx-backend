#!/usr/bin/python3
""" LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ A class LIFOCache that inherits
    from BaseCaching and is a caching system """

    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data[key] = item
                else:
                    self.cache_data.pop(self.stack[-1])
                    print("DISCARD: {}".format(self.stack[-1]))
                    self.stack.pop(-1)
            else:
                self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        self.stack.remove(key)
        self.stack.append(key)
        return self.cache_data[key]
