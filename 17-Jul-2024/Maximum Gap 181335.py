# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            _max = max(_max, nums[i+1] -nums[i])
        return _max