# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        di = defaultdict(list)
        def t(elem):
            return (elem[1], elem[0])
        def helper(root,r,c):
            if not root :return

            di[c].append([root.val,r])
            helper(root.left,r+1,c-1)
            helper(root.right,r+1,c+1)
        helper(root,0,0)
        x = list(di.items())
        # print(x)
        x.sort()
        # print(x)
        ans = []
        for i in x:
            ar = i[1]
            ar.sort(key = t)
            # print(ar)
            ans.append([num for num,j in ar])
        return ans