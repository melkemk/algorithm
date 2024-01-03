class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        i=0
        ans,right=0,len(nums)-1
        while(i<=right):
            ans+=1
            if nums[i]+nums[right]<=limit:
                i+=1
                right-=1
            else:
                right-=1
        # if i==len(nums):return ans+1
        return ans 