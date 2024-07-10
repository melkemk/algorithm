# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = deque([root]) if root else None
        ans = []
        while queue:
            ans.append(queue[-1].val)
            for _ in range(len(queue)):
                last = queue.popleft()
                if last.left :queue.append(last.left)
                if last.right :queue.append(last.right)

        return ans 




