# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def trav(root,_max,_min):
            if not root: return _max-_min
            _max = max(root.val,_max)
            _min = min(root.val,_min)
            return max(trav(root.left,_max,_min),trav(root.right,_max,_min))
        return trav(root,-inf,inf)