# 0169 · Majority Element

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | array · hash-table · divide-and-conquer · sorting · counting | **Python3** · 1 ms · 19.3 MB | 2025-06-15 08:39 UTC |

---

## Problem Statement
https://leetcode.com/problems/majority-element

---

## Approach
Boyer–Moore Majority Vote. A single candidate and the corresponding balance is maintained where each candidate appearance increments the balance and each non-candidate appearance decrements the balance. The candidate is only replaced with the current number if the balance reaches 0. Because the majority element appears more than ⌊n/2⌋ times, it cannot be completely cancelled out by other elements, ensuring that the majority element will always be the final candidate.

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(1) |

---

## Code

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, balance = None, 0
        for num in nums:
            if num == candidate:
                balance += 1  # increment balance for every candidate
            else:
                if balance > 0:  # decrement balance for every non-candidate
                    balance -= 1
                else:  # replace candidate if balance <= 0 (i.e., non-candidates have appeared more than the candidate so far)
                    candidate = num
                    balance = 1
        return candidate

```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 1 ms | 19.3 MB | 87.15 % time · 87.2 % memory | [View](https://leetcode.com/problems/majority-element/submissions/1664746088/) |
