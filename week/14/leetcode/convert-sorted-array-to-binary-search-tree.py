# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    
        def insert(l,r):
            if l>r:
                return None
            middle = (l + r )//2
            
            left = insert(l,middle-1)
            right = insert(middle+1,r)
            head = TreeNode(nums[middle],left,right)
            return head
        return insert(0,len(nums)-1)