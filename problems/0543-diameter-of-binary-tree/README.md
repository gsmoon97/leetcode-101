# 0543 · Diameter of Binary Tree

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | tree · depth-first-search · binary-tree | **Python3** · 4 ms · 20.6 MB | 2025-06-15 11:20 UTC |

---

## Problem Statement
https://leetcode.com/problems/diameter-of-binary-tree/description/

---

## Approach
Post-order DFS returns each node’s left/right heights in edges and updates a global maximum with their sum, yielding the tree’s diameter in one linear pass.

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        # post-order traversal (evaluate children before parent)
        # sum the longest heights (inclusive) for each subtree (left and right)
        # height(node) = number of edges on the longest path from this node down to any leaf
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            self.diameter = max(self.diameter, lh + rh)
            return max(lh, rh) + 1
        height(root)
        return self.diameter
        
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 4 ms | 20.6 MB | 74.08 % time · 98.61 % memory | [View](https://leetcode.com/problems/diameter-of-binary-tree/submissions/1664862434/) |
