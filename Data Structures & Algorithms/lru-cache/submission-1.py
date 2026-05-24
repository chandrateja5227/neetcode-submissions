class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRUCache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.LRUCache:
            self.LRUCache.move_to_end(key)
            return self.LRUCache[key]
       
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache:
            self.LRUCache.move_to_end(key)
        self.LRUCache[key] = value
        if len(self.LRUCache) > self.capacity:
            self.LRUCache.popitem(last=False)