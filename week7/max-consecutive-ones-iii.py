class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
     left=0
     flipped,_max=0,0
     for right in range(len(nums)):
         if nums[right]==0:flipped+=1
         while flipped>k:
             if nums[left]==0:
                 flipped-=1
             left+=1
         _max=max(_max,right-left+1)
     return _max
