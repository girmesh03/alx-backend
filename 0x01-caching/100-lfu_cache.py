#!/usr/bin/python3
""" LFU Caching """


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ A class LFUCache that inherits
    from BaseCaching and is a caching system """

    def __init__(self):
        """ Initialize LFU Caching """
        super().__init__()
        self.lfu = []
        self.lfu_count = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lfu_count[key] += 1
                self.lfu.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    min_value = min(self.lfu_count.values())
                    min_keys = [k for k in self.lfu_count
                                if self.lfu_count[k] == min_value]
                    if len(min_keys) > 1:
                        for k in self.lfu:
                            if k in min_keys:
                                self.cache_data.pop(k)
                                self.lfu_count.pop(k)
                                self.lfu.remove(k)
                                break
                    else:
                        self.cache_data.pop(min_keys[0])
                        self.lfu_count.pop(min_keys[0])
                        self.lfu.remove(min_keys[0])
                        print("DISCARD: {}".format(min_keys[0]))
                self.cache_data[key] = item
                self.lfu_count[key] = 0
            self.lfu.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        self.lfu_count[key] += 1
        self.lfu.remove(key)
        self.lfu.append(key)
        return self.cache_data[key]
