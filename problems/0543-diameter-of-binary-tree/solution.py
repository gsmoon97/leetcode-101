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
        