# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.accumelate = []
        def sumn(root,ar):
            if not root:return 
            if not root.left and not root.right:
                # if ar :
                ar.append(root.val)
                self.accumelate.append(int("".join(str(i) for i in  ar)))
                return
            ar.append(root.val)
            sumn(root.left,ar[::])
            sumn(root.right,ar[::])
        sumn(root,[])
        return sum(self.accumelate)