# 0236 · Lowest Common Ancestor of a Binary Tree

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | tree · depth-first-search · binary-tree | **Python3** · 32 ms · 22.1 MB | 2025-09-08 01:01 UTC |

---

## Problem Statement
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

---

## Approach
Recursive DFS: Recursively traverse the left and right subtree to verify if the subtree contain either `p` or `q`. Key assumption is that if both left and right subtrees return non-null values, the current node is the LCA. Propogate this LCA to the root. Even if `p` or `q` happens to be the ancestor of the other node, there is no need to traverse the subtree of the ancestor node since the LCA will be `p` or `q` respectively.

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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            # Even if `p` or `q` happens to be the ancestor of the other node,
            # there is no need to traverse the subtree of the ancestor node
            # since the LCA will be `p` or `q` respectively
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If `p` and `q` are both found in the current node's subtrees
        # the current node is the LCA
        if left and right:
            return root
        
        return left if left else right


```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 32 ms | 22.1 MB | 99.77 % time · 44.17 % memory | [View](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1763200291/) |
