# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nums = []
        
        def recc(root):
            if not root:return None
            recc(root.left)
            nums.append(root.val)
            recc(root.right)
        recc(root)
        def insert(l,r):
            if l>r:
                return None
            middle = (l + r )//2
            
            left = insert(l,middle-1)
            right = insert(middle+1,r)
            head = TreeNode(nums[middle],left,right)
            return head
        return insert(0,len(nums)-1)
                    
                    
        # return rec(None,0,len(nums)-1)