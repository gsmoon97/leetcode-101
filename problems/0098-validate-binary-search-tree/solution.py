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