class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l=[0]
        def rec(root):
            if root is None:
                return
            rec(root.left)
            l.append(root.val)
            rec(root.right)
        rec(root)
        return l[k]
