class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = [0]*len(grid)
        cols = [0] * len(grid[0])
        for i,row in enumerate(grid):
            rows[i] =max(row)
        for i,row in enumerate(list(zip(*grid))):
            cols[i] =max(row)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += ( min(rows[i],cols[j]) -grid[i][j] )
        return ans
        