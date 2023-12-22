class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        for i in range(len(matrix)):
            for j in range(0,i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        print(matrix)
        for col in range(len(matrix)):
            matrix[col]=matrix[col][::-1]