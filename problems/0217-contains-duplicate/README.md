# 0217 · Contains Duplicate

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | array · hash-table · sorting | **Python3** · 11 ms · 31.6 MB | 2025-06-15 12:09 UTC |

---

## Problem Statement
https://leetcode.com/problems/contains-duplicate/description/

---

## Approach
One-pass with a hash set to track previously seen numbers

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(n) |

---

## Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        has_seen = set()
        for num in nums:
            if num in has_seen:
                return True
            has_seen.add(num)
        return False
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 11 ms | 31.6 MB | 76.07 % time · 53.52 % memory | [View](https://leetcode.com/problems/contains-duplicate/submissions/1664906448/) |
