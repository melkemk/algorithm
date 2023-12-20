class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maximum=0
        for i in range(0,len(grid[0])-2):
            for j in range(0,len(grid)-2):
                check=0
                m=0
                for row in range(j,j+3):
                    for col in range(i,i+3):
                        if  not (check==3 or check==5):
                            print(grid[row][col])
                            m+=grid[row][col]
                        check+=1
                maximum=max(maximum,m)
        return maximum



            