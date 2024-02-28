# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root,val):
            if not root:return 
            if root.val>val:
                root.left = delete(root.left,val)
                return root
            elif root.val<val:
                root.right = delete(root.right,val)
                return root
            elif root.val == val:
                if not root.left and not root.right:
                    return None
                if not root.left:
                    root = root.right
                    return root
                if not root.right:
                    root = root.left
                    return root
                x = root
                x= x.right
                while x.left :
                    x = x.left
                root.val = x.val

                # the x node will now become the new target
                root.right = delete(root.right,x.val)
                return root
                
        return delete(root,key)
            