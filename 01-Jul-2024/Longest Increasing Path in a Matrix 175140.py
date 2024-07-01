# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dir = {(0,-1),(-1,0),(0,1),(1,0)}
        visited = set()
        def inbound(r,c):
            return 0<=r<len(matrix) and 0<=c<len(matrix[0])
        @cache
        def dfs(i,j):
            _max = 1
            for x,y in dir:
                x += i
                y += j
                if inbound(x,y) and matrix[x][y]>matrix[i][j]:
                    _max = max(_max,dfs(x,y)+1)
            return _max
        ans = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans,dfs(i,j))
        return ans 