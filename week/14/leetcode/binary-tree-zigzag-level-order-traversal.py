# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = defaultdict(list)
        def helper(root,inx):
            if not root :return 
            self.ans[inx].append(root.val)
            helper(root.left,inx+1)
            helper(root.right,inx+1)
        helper(root,0)
        # print(self.ans)

                
        return list(list(reversed(j)) if i%2  else j for i,j in   self.ans.items())
