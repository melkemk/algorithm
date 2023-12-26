class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        x,j=0,0
        for i in range(len(mat)):
            x+=mat[i][j]
            j+=1
        j=len(mat)-1
        i=0
        while j>-1:
            x+=mat[j][i]
            i+=1
            j-=1
        return x if not len(mat)%2 else x-mat[len(mat)//2][len(mat)//2]