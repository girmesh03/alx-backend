#!/usr/bin/python3
""" FIFO Caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ A class FIFOCache that inherits
    from BaseCaching and is a caching system """

    def __init__(self):
        """ Initialize FIFOCache """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data[key] = item
                else:
                    self.cache_data.pop(self.queue[0])
                    print("DISCARD: {}".format(self.queue[0]))
                    self.queue.pop(0)
            else:
                self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
