# 0226 · Invert Binary Tree

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | tree · depth-first-search · breadth-first-search · binary-tree | **Python3** · 0 ms · 17.9 MB | 2025-06-07 14:39 UTC |

---

## Problem Statement
https://leetcode.com/problems/invert-binary-tree

---

## Approach
DFS with recursion

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)  # recursion
        return root  
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 17.9 MB | 100.0 % time · 31.65 % memory | [View](https://leetcode.com/problems/invert-binary-tree/submissions/1656634563/) |
