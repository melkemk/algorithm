class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans=0
        for i in range(len(nums)):
            r=i+1
            while(r<len(nums)):
                if nums[i]+nums[r]<target:ans+=1
                r+=1
        return ans