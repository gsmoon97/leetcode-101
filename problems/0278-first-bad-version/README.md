# 0278 · First Bad Version

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | binary-search · interactive | **Python3** · 36 ms · 17.7 MB | 2025-06-14 12:49 UTC |

---

## Problem Statement
https://leetcode.com/problems/first-bad-version/description/

---

## Approach
Binary search to halve the candidate interval per iteration until the two pointers converge.

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(log n) | O(1) |

---

## Code

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary search
        # half the search space per iteration until the start and end pointers converge
        start, end = 1, n
        while start < end:
            query = start + (end - start) // 2
            if isBadVersion(query):
                end = query
            else:
                start = query + 1
        return end
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 36 ms | 17.7 MB | 67.28 % time · 44.95 % memory | [View](https://leetcode.com/problems/first-bad-version/submissions/1663850854/) |
