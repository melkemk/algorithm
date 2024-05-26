# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix),len(matrix[0])
        def inbound(i,j):return 0<=i<n and 0<=j<m
        dir = [(1,1),(1,0),(0,1)]
        @cache
        def dp(i,j):
            if not inbound(i,j):return 0 
            ar = [] 
            for x,y in dir:
                ar.append(dp(x+i,y+j)**0.5)
            return (int(matrix[i][j]) + min(ar))**2 if int(matrix[i][j])  else 0 
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans,dp(i,j))
        return int(ans)
