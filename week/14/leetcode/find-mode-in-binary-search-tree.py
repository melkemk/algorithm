# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = Counter()

        def find(root):
            if not root :return 
            find(root.left)
            find(root.right)
            counter[root.val] += 1
        find(root)
        max_value = max(counter.values())
        return list(i for i in counter if counter[i]==max_value)


