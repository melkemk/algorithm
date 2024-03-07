class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def possible(total):
            thre = 0
            i = 0
            while i <(len(nums)): 
                thre += ceil(nums[i]/total)
                if thre >threshold :return 0 
                i += 1
            return thre<=threshold
        low  ,high = 1,max(nums)
        while low <= high:
            mid = low + (high - low)//2
            # print(canEat(mid),mid)
            if possible(mid):
                high = mid-1
            else:
                low = mid+1
        return low
                