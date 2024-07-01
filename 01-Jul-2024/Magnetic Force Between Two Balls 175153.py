# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l,r = 1,10**9
        def check(mid):
            temp = m-1
            last = position[0]
            for i in position:
                if i-last>=mid: 
                    temp-=1
                    last = i
            return temp<=0 
        while l<=r:
            mid = (l+r)//2
            if check(mid):
                l = mid+1
            else: 
                r = mid-1 
        return r
 

        