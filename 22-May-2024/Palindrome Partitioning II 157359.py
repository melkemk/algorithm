# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def dp(i):
            if i==len(s): 
                return 0 
            t = inf
            for j in range(len(s),i,-1):
                if s[i:j] ==s[i:j][::-1]: 
                    t = min(t,  1 + dp(j) )
            return t 

        return dp(0)-1