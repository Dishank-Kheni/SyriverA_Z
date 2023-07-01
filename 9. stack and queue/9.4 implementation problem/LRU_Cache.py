from collections import deque


class LRUCache():

    def __init__(self, capacity) -> None:
        self.cache = {}
        # deque()
        self.capacity = capacity

    def update_getCache(self, key):
        if key in self.cache:
            self.update_putCache(key, self.cache[key])
            return self.cache[key]
        else:
            return -1

    def update_putCache(self, key, val):
        if len(self.cache) < self.capacity:
            self.cache[key] = val
        elif key in self.cache:
            self.cache.pop(key)
            self.cache[key] = val
            # pass
        else:
            for k in self.cache.keys():
                self.cache.pop(k)
                break
            self.cache[key] = val

    def get(self, key):
        return self.update_getCache(key)

    def put(self, key, value):
        self.update_putCache(key, value)


if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(1))  # return 1
    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2))    # returns -1 (not found)
    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1))    # return -1 (not found)
    print(lRUCache.get(3))    # return 3
    print(lRUCache.get(4))    # return 4
