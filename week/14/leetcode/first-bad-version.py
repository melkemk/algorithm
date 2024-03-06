# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l,r = 0,n
        m = 0 
        while l<=r:
            m = (l+r)//2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m +1 

        return m if isBadVersion(m) else m +1
        