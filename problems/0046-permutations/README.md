# 0046 · Permutations

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · backtracking | **Python3** · 0 ms · 18.0 MB | 2025-09-07 04:24 UTC |

---

## Problem Statement
https://leetcode.com/problems/permutations/

---

## Approach
Backtracking: Initialize a list `used` to keep track of whether each number was included in the running permutation or not. 1) Choose a number to include in the permutation. 2) Explore all possible sub-permutations. 3) Backtrack the number for the next iteration.

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n! x n) | O(n) |

---

## Code

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        N = len(nums)
        permutations = []
        def backtrack(permutation: List[int], used: List[bool]):
            if len(permutation) == N:
                permutations.append(permutation.copy())
                return
            for i in range(N):
                if used[i]:  # check if current number has been used already
                    continue
                
                # choose the current number
                permutation.append(nums[i])
                used[i] = True
                
                # explore all possible sub-permutations
                backtrack(permutation, used)
                
                # backtrack the current number for the next iteration
                permutation.pop()
                used[i] = False
            return

        backtrack([], [False] * N)  # initialize
        return permutations
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 18.0 MB | 100.0 % time · 58.91 % memory | [View](https://leetcode.com/problems/permutations/submissions/1762208633/) |
