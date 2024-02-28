# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val<p.val:p,q=q,p
        def rec(node,p,q):
            if not node:return 
            # print(node.val,q.val,p.val)
            if node.val ==q.val or  node.val ==p.val or  p.val<node.val<q.val  :
                return node
            if node.val>q.val:
                return (rec(node.left,p,q))
            elif node.val<p.val:
                return (rec(node.right,p,q))

        # print()
        return rec(root,p,q)

