class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self._set = set()
        def helper(i,j,idx):
            # print(self._set,i,j,idx)
            if idx ==len(word):
                # print(self._set,idx)
                return 1
            if i>=len(board) or j>=len(board[0]) or i<0 or j <0 or  (i,j) in  self._set :
                return 0

            if  idx < len(word) and board[i][j] != word[idx]:
                # print(idx,i,j)
                return 0
            idx += 1

            self._set.add((i,j))
            a = helper(i,j-1,idx )
            b = helper(i+1,j,idx )
            c = helper(i-1,j,idx )  
            d = helper(i,j+1,idx )  
            self._set.remove((i,j))
            return max(a,b,c,d)

        for i in range(len(board)):
            for j in range(len(board[0])):
                    if helper(i,j,0 )  :return 1