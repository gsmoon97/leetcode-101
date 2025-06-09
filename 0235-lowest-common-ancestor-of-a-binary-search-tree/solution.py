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