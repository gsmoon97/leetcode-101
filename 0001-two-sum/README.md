# 0001 · Two Sum

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | array · hash-table | **Python3** · 0 ms · 18.9 MB | 2025-06-03 19:08 UTC |

---

## Problem Statement
https://leetcode.com/problems/two-sum

---

## Approach
One-pass hash map

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(n) |

---

## Code

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}  # value -> index

        for i, num in enumerate(nums):
            j = seen.get(target - num)  # index of complement if present
            if j is not None:
                return [j, i]  # earlier index first
            seen[num] = i  # store the current value

        # Problem guarantees a solution, but good practice:
        raise ValueError("No two sum solution")

```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 18.9 MB | 100.0 % time · 33.86 % memory | [View](https://leetcode.com/problems/two-sum/submissions/1651054846/) |
