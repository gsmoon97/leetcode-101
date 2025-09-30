class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.access_record = deque()

    def get(self, key: int) -> int:
        value = -1
        if key in self.cache:
            value = self.cache[key]
            self.access_record.append(key)  # indicate that the key was accessed most recently
        # print(self.cache)
        # print(self.access_record)
        # print('='*10)
        return value

    def put(self, key: int, value: int) -> None:
        self.access_record.append(key)  # indicate that the key was accessed most recently
        if len(self.cache) < self.capacity:  # cache not full yet
            self.cache[key] = value
        elif key in self.cache:  # cache full but key exists already
            self.cache[key] = value
        else:  # cache full & key does not exist-> evict LRU key
            lru_key = self.access_record.popleft()
            while lru_key in self.access_record:  # necessary in case lru key has been accessed more recently again
                lru_key = self.access_record.popleft()  
            del self.cache[lru_key]  # evict the key
            self.cache[key] = value
        # print(self.cache)
        # print(self.access_record)
        # print('='*10)
        return



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)