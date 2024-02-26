# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root and   not root.left and not root.right:return 1
        if not root.left or not root.right:return 0
        def isSymmetric(left,right):
            if not left and not right:return 1
            if not left or not right:return 0
            if left.val !=right.val:return 0 
            return min(isSymmetric(left.left,right.right),isSymmetric(left.right,right.left))
        return isSymmetric(root.left,root.right)