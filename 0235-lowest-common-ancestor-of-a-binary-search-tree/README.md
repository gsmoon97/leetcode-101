# 0235 · Lowest Common Ancestor of a Binary Search Tree

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | tree · depth-first-search · binary-search-tree · binary-tree | **Python3** · 57 ms · 21.0 MB | 2025-06-09 18:07 UTC |

---

## Problem Statement
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

---

## Approach
One-pass walk down the BST from the root until no longer can traverse to the same subtree for both p and q (i.e., first point of divergence is the LCA)

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(h) | O(1) |

---

## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # ensure p.val < q.val for easier comparison
        if p.val > q.val:
            p, q = q, p
        # LCA when can no longer traverse to the same subtree for both p and q
        node = root
        while True:
            if q.val < node.val:
                node = node.left
            elif node.val < p.val:
                node = node.right
            else:
                return node
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 57 ms | 21.0 MB | 65.35 % time · 81.28 % memory | [View](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/1658937979/) |
