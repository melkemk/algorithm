# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0 
        def helper(root):
            if not root:return 
            if low <=  root.val<= high:
                self.ans += root.val
            helper(root.right)
            helper(root.left)
        helper(root)
        return self.ans