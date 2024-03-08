# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        di = defaultdict(list)
        def rec(root,r,c):
            if not root.left and not root.right:
                return
            if root.left:
                di[r].append((2*c))                
                rec(root.left,r+1,  2*c )
            if root.right : 
                print(root.val,c)
                di[r].append((2*c)+1)                
                rec(root.right,r+1,  (2*c)+1)
        rec(root,0,1)
        _max =  1
        print(di)
        for i,j in di.items():
            _max = max(j[-1]-j[0]+1 ,_max)
        return _max