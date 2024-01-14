from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre = 0
        l = 0
        ans = float('inf')  # Initialize ans with positive infinity
        i = 0

        while i < len(nums):
            pre += nums[i]

            while pre >= target:
                ans = min(ans, i - l + 1)
                pre -= nums[l]
                l += 1

            i += 1

        return ans if ans != float('inf') else 0
