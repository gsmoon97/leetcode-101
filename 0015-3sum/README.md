# 0015 · 3Sum

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · two-pointers · sorting | **Python3** · 463 ms · 20.7 MB | 2025-08-31 02:48 UTC |

---

## Problem Statement
https://leetcode.com/problems/3sum/description/

---

## Approach
Sorting & Two-Pointers: Sort the list first, then iterate through each element using two-pointers on the remaining elements to find the optimal two sum that complements the current element to sum upto 0.

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n^2) | O(1) |

---

## Code

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort the numbers first to use two pointers later
        triplets = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:  # to skip duplicates
                continue
            target = -1 * nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum < target:
                    left += 1
                elif two_sum > target:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    # Skip duplicates for right  
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return triplets
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 463 ms | 20.7 MB | 85.29 % time · 36.02 % memory | [View](https://leetcode.com/problems/3sum/submissions/1754188800/) |
