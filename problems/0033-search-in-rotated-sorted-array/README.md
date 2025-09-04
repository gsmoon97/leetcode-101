# 0033 · Search in Rotated Sorted Array

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · binary-search | **Python3** · 0 ms · 18.0 MB | 2025-09-04 21:10 UTC |

---

## Problem Statement
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

---

## Approach
Variation of Binary Search: Key observation is that for any arbitrary pivot, at least one half is always sorted. For each iteration, we halve the search space by making use of this sorted half to check if the target would be in the sorted half or the other half.

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
        # key observation: for any arbitrary pivot, at least one half is always sorted
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:  # left side is the sorted half
                if nums[left] <= target < nums[mid]:  # target must be in the sorted half, if it exists 
                    right = mid - 1
                else:  # target must be in the unsorted half, if it exists
                    left = mid + 1
            elif nums[mid] <= nums[right]:  # right side is the sorted half
                if nums[mid] < target <= nums[right]:  # target must be in the sorted half, if it exists 
                    left = mid + 1
                else:  # target must be in the unsorted half, if it exists
                    right = mid - 1
        return -1
            



```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 18.0 MB | 100.0 % time · 90.95 % memory | [View](https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1759846700/) |
