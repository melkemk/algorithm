class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=len(nums)
        left=0
        right=0
        while(right<l):
            while( right<l-1 and nums[right]==0):
                right+=1
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right+=1
        return nums