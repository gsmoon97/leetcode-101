# 0981 · Time Based Key-Value Store

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | hash-table · string · binary-search · design | **Python3** · 154 ms · 74.6 MB | 2025-09-08 03:57 UTC |

---

## Problem Statement
https://leetcode.com/problems/time-based-key-value-store/description/

---

## Approach
Hash Table & Binary Search: Hash Table to map 'key' with ('timestamp_i', 'value_i'). Binary Search to find the largest `timestamp_prev` <= `timestamp` and 'get' the corresponding value.

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | set: O(1); get: O(log n) where n = total number of timestamps for input `key` | O(m) where m = total number of `set` operations |

---

## Code

```python
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
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 154 ms | 74.6 MB | 22.0 % time · 42.76 % memory | [View](https://leetcode.com/problems/time-based-key-value-store/submissions/1763293278/) |
