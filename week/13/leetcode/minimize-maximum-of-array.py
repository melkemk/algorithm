class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        running = 0 
        _max = nums[0]
        for i ,j in enumerate(nums):
            running += j
            if j>_max:
                _max = max(ceil(running/(i+1)),_max)
        return _max