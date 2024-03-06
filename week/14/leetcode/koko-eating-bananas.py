class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        def canEat(total):
            hour = 0
            i = 0
            while i <(len(piles)): 
                hour += ceil(piles[i]/total)
                if hour > h:return 0 
                i += 1
            return hour<=h
        low  ,high = 1,sum(piles)
        while low <= high:
            mid = low + (high - low)//2
            # print(canEat(mid),mid)
            if canEat(mid):
                high = mid-1
            else:
                low = mid+1
        return low
                