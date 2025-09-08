# 0075 · Sort Colors

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · two-pointers · sorting | **Python3** · 0 ms · 17.8 MB | 2025-09-08 22:08 UTC |

---

## Problem Statement
https://leetcode.com/problems/sort-colors/description/

---

## Approach
Three-Pointers (a.k.a. Dutch National Flag Algorithm): 1) `i` to keep track of the current index 2) `left` to keep track of where 0 should be placed 3) `right` to keep track of where 2 should be placed

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(1) | O(1) |

---

## Code

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch national flag algorithm
        # Invariants: 
        # 1) 0 <= all 0s <= left  
        # 2) left < all 1s <= i 
        # 3) i < unknown < right
        # 4) right <= all 2s < end
        i = 0
        left = 0
        right = len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                # do not increment `i` yet since we don't know if the swapped element is 0 yet
            else:  # nums[i] == 1
                i += 1

```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 17.8 MB | 100.0 % time · 53.76 % memory | [View](https://leetcode.com/problems/sort-colors/submissions/1764322733/) |
