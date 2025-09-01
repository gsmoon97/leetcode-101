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
