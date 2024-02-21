class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0
        i = 0
        if len(nums)==1:return True
        for i in range(len(nums)-1):
            step=max(nums[i]+i,step)

            if step==i:
                return False
            print(step)
        return True

            