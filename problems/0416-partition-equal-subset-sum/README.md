# 0416 · Partition Equal Subset Sum

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · dynamic-programming · backtracking | **Python3** · 554 ms · 18.0 MB | 2025-09-09 02:10 UTC |

---

## Problem Statement
https://leetcode.com/problems/partition-equal-subset-sum/description/

---

## Approach
DP (Bottom-Up): Formulate as a 0/1 Knapsack Problem. Iterate over all `nums` and update `dp` to be `dp[i] or dp[i - num]`. For each `num`, traverse `i` backwards to prevent using the same element twice.

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n x s) where n = number of numbers, s = target sum | O(n) where n = number of numbers |

---

## Code

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Formulate as a 0/1 Knapsack Problem
        total_sum = sum(nums)
        if total_sum % 2 != 0:  # early termination for odd total sum
            return False
        target_sum = total_sum // 2
        
        # DP: Bottom-Up with iteration
        dp = [False] * (target_sum + 1)
        dp[0] = True  # sum 0 is achievable without using any numbers

        for num in nums:
            for i in range(target_sum, num - 1, -1):  # traverse backwards to prevent using the same `num`
                dp[i] = dp[i] or dp[i-num]
        
        return dp[target_sum]
        
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 554 ms | 18.0 MB | 67.85 % time · 74.56 % memory | [View](https://leetcode.com/problems/partition-equal-subset-sum/submissions/1764419817/) |
