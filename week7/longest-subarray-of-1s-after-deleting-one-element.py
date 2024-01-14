class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
       left=0
       _max=0
       zero=0
       for right in range(len(nums)):
           if nums[right]==0:zero+=1
           while left<len(nums) and zero>1:
               if nums[left]==0:
                   zero-=1
               left+=1
           _max=max(_max,right-left)
       return _max