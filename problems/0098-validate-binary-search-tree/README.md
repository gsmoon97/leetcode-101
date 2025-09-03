# 0098 · Validate Binary Search Tree

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | tree · depth-first-search · binary-search-tree · binary-tree | **Python3** · 2 ms · 19.8 MB | 2025-09-03 03:55 UTC |

---

## Problem Statement
https://leetcode.com/problems/validate-binary-search-tree/description/

---

## Approach
Range-based Validation: Keep track of `min_val` and `max_val` to specify the valid range in which the child node value must be within (exclusive) based on the assumption that each node must be within a valid range based on its ancestors.

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(h) |

---

## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # each node must be within a valid range based on its ancestors
        def validate(node, min_val, max_val) -> bool:
            if not node:  # empty trees are valid BSTs
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
        return validate(root, float('-inf'), float('inf'))
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 2 ms | 19.8 MB | 39.17 % time · 29.6 % memory | [View](https://leetcode.com/problems/validate-binary-search-tree/submissions/1757739339/) |
