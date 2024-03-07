class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans ,i= 0 ,0
        nums.sort()
        while i < len(nums):
            x = bisect_right(nums,target-nums[i])
            if  x <= i:
                break
            ans += 2**(x-i-1)
            i += 1
        return ans %  (10**9 + 7)
                
            
