class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canTransfer(total):
            day = 0
            temp = 0 
            for i in weights:
                if temp + i >total:
                    day += 1
                    temp = 0 
                if i >total:return 0
                temp += i
            day += 1
            return day<=days

        low  ,high = 1,sum(weights)
        while low <= high:
            mid = low + (high - low)//2
            if canTransfer(mid):
                high = mid-1
            else:
                low = mid+1
        return low
                