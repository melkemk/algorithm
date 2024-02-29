class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l=[]
        def rec(root):
            if root is None:
                return
            rec(root.left)
            l.append(root.val)
            rec(root.right)
        rec(root)
        return sorted(l)==l and len(l)==len(set(l))

