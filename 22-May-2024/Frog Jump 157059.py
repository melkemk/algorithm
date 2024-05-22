# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def dp(i,j,l):
            if i==len(stones)-1:
                return j ==stones[i]
            if i==len(stones):return 0 
            if j > stones[i]:
                return dp(bisect_left(stones,j),j,l)
            if j==stones[i]:return  max(dp(i+1,j+l-1,l-1),dp(i+1,j+l,l),dp(i+1,j+1+l,l+1))
            return 0 
        return dp(1,1,1)