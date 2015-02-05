class LRUCache:
    
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    # @return an integer
    def get(self, key):
        if key in self.cache:
            val = self.cache[key]
            del self.cache[key] # Place to the tail as recent used
            self.cache[key] = val
            return val
        else:
            return -1
            
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            del self.cache[key]
            
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
            
        self.cache[key] = value
        