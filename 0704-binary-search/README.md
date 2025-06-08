# 0704 · Binary Search

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | array · binary-search | **Python3** · 0 ms · 18.9 MB | 2025-06-08 03:12 UTC |

---

## Problem Statement
https://leetcode.com/problems/binary-search

---

## Approach
Binary search

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(log n) | O(1) |

---

## Code

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_idx = 0
        r_idx = len(nums) - 1
        while l_idx <= r_idx:
            m_idx = l_idx + (r_idx - l_idx) // 2  # overflow-safe pattern
            mid = nums[m_idx]
            if target == mid:
                return m_idx
            if target < mid:
                r_idx = m_idx - 1
            else:
                l_idx = m_idx + 1
        return -1

```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 18.9 MB | 100.0 % time · 6.33 % memory | [View](https://leetcode.com/problems/binary-search/submissions/1657203855/) |
