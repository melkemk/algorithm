class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def possible(total):
            j,i  = 0 ,0
            while i < (len(houses)):
                if j<len(heaters) and abs(houses[i] -heaters[j])>total:
                    j += 1
                else:
                    i += 1
                if j >=len(heaters) and i<len(houses):
                    return 0 
            return 1

        low  ,high = 0,max(houses) +heaters[-1]
        ans = high
        while low <= high:
            mid = low + (high - low)//2
            if possible(mid):
                high = mid-1
                ans = mid
            else:
                low = mid+1
        return ans