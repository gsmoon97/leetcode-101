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
