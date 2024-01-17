class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        right=sum(nums)
        left=0
        for i,j in enumerate(nums):
            print(right,left)
            if right-j==left:return i
            right-=j
            left+=j
        return  -1