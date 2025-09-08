class TimeMap:

    def __init__(self):
        self.store = {}  # `key` : [(`timestamp_1`, `value_1`), ..., (`timestamp_t`, `value_t`)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        tv_list = self.store.setdefault(key, [])
        tv_list.append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        result = ""

        if key not in self.store:
            return result

        values = self.store[key]
        # binary search
        low, high = 0, len(values) - 1
        while low <= high:
            mid = low + (high - low) //2
            if values[mid][0] <= timestamp:
                result = values[mid][1]  # update when `timestamp_prev` <= `timestamp`
                low = mid + 1
            else:
                high = mid - 1
        return result



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)