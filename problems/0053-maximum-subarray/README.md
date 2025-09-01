# 0053 · Maximum Subarray

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · divide-and-conquer · dynamic-programming | **Python3** · 63 ms · 32.5 MB | 2025-06-22 16:28 UTC |

---

## Problem Statement
https://leetcode.com/problems/maximum-subarray/description/

---

## Approach
Kadane's Algorithm: keeps track of the maximum subarray sum ending at each position, and updates a global maximum as it goes

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(1) |

---

## Code

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        max_sum = running_sum = nums[0]
        for num in nums[1:]:
            if num > (running_sum + num):  # only reset the running sum if the current number is larger than current number + running sum
                running_sum = num
            else:
                running_sum += num  # otherwise, add the current number to the running sum
            max_sum = max(max_sum, running_sum)
        return max_sum
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 63 ms | 32.5 MB | 57.63 % time · 51.33 % memory | [View](https://leetcode.com/problems/maximum-subarray/submissions/1672834114/) |
