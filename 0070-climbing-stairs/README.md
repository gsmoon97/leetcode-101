# 0070 · Climbing Stairs

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | math · dynamic-programming · memoization | **Python3** · 0 ms · 17.9 MB | 2025-06-14 16:54 UTC |

---

## Problem Statement
https://leetcode.com/problems/climbing-stairs/

---

## Approach
Bottom-up iteration of Fibonacci sequence where f(n) = f(n-1) + f(n-2) (since top-down recursion leads to stack limit)

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(1) |

---

## Code

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            # return self.climbStairs(n-1) + self.climbStairs(n-2)  # top-down recursion leads to stck limit
            prev_prev, prev = 2, 3
            for _ in range(4, n+1):
                prev_prev, prev = prev, prev_prev + prev
            return prev
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 17.9 MB | 100.0 % time · 30.15 % memory | [View](https://leetcode.com/problems/climbing-stairs/submissions/1664045983/) |
