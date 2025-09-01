# 0102 · Binary Tree Level Order Traversal

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | tree · breadth-first-search · binary-tree | **Python3** · 1 ms · 18.5 MB | 2025-08-26 16:36 UTC |

---

## Problem Statement
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

---

## Approach
Iterative BFS using queue with a additional variable to keep track of the current level

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(n) |

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        nodes = []
        while queue:
            node, lvl = queue.popleft()
            if node:
                if len(nodes) == lvl:
                    nodes.append([node.val])
                else:
                    nodes[lvl].append(node.val)
                queue.append((node.left, lvl + 1))
                queue.append((node.right, lvl + 1))
        return nodes

```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 1 ms | 18.5 MB | 29.83 % time · 38.64 % memory | [View](https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1749218000/) |
