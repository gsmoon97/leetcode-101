# 0110 · Balanced Binary Tree

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | tree · depth-first-search · binary-tree | **Python3** · 3 ms · 18.9 MB | 2025-06-11 20:28 UTC |

---

## Problem Statement
https://leetcode.com/problems/balanced-binary-tree

---

## Approach
A single post-order DFS (children first, parent last)

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> tuple[int, bool]:
            if not node:
                return 0, True
            # post-order dfs (evaluate children first)
            l_height, l_balanced = dfs(node.left)
            r_height, r_balanced = dfs(node.right)
            # any imbalances in sub-trees propagate upwards
            balanced = l_balanced and r_balanced and abs(r_height - l_height) <= 1
            return 1 + max(l_height, r_height), balanced
        return dfs(root)[1]
        
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 3 ms | 18.9 MB | 67.05 % time · 27.25 % memory | [View](https://leetcode.com/problems/balanced-binary-tree/submissions/1661231044/) |
