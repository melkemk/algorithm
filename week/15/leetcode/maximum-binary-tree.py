# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def insert(l,r):
            if l> r:
                return None
            ind = l+nums[l:r+1].index(max(nums[l:r+1]))
            left = insert(l,ind-1)
            right = insert(ind+1,r)
            node = TreeNode(nums[ind],left,right)
            return node
        return insert(0,len(nums)-1)
                    