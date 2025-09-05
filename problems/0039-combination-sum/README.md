# 0039 · Combination Sum

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · backtracking | **Python3** · 5 ms · 17.7 MB | 2025-09-05 05:27 UTC |

---

## Problem Statement
https://leetcode.com/problems/combination-sum/description/

---

## Approach
Backtracking: Backtracking is more suitable than DP for this type of problem since the task is to find all possible combinations. Implement backtrack logic to find all possible combinations that sum up to `target` without any duplicate combinations, where N=number of candidates, T=target value, M=minimum candidate value .

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(N ^ (T/M)) | O(T/M) |

---

## Code

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # DP is more suitable for counting/checking existence
        # Backtracking is more suitable for this type of problem since the task is to find all possible combinations
        all_combinations = []

        def backtrack(remaining_target, combinations, start_idx):  # helper function to backtrack all possible sub-combinations
            if remaining_target < 0:  # invalid combination
                return
            if remaining_target == 0:  # valid combination
                all_combinations.append(combinations.copy())  # copy() the list to prevent mutating the shared list
                return
            for i in range(start_idx, len(candidates)):  # add more numbers to find valid combination that sum upto `target`
                combinations.append(candidates[i])  # try building combination initialized with the current candidate as the first element
                backtrack(remaining_target - candidates[i], combinations, i)  # `start_idx` to prevent duplicates
                combinations.pop()  # backtracks
            return combinations
        
        backtrack(target, [], 0)
        return all_combinations
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 5 ms | 17.7 MB | 87.11 % time · 87.83 % memory | [View](https://leetcode.com/problems/combination-sum/submissions/1760075452/) |
