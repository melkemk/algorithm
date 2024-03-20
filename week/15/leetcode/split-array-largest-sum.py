class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canTransfer(total):
            day = 0
            temp = 0 
            for i in nums:
                if temp + i >total:
                    day += 1
                    temp = 0 
                temp += i
            day += 1
            return day<=k

        low  ,high = max(nums),sum(nums)
        while low <= high:
            mid = low + (high - low)//2
            if canTransfer(mid):
                high = mid-1
            else:
                low = mid+1
        return low
                