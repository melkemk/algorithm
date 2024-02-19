class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans , _sum , left =-inf,0 , 0
        for right in range(len(nums)):
            _sum += nums[right]
            ans = max(_sum,ans)
            if _sum < 0:
                left = right+1
                _sum = 0
        return ans