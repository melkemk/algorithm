class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sol = []
        def validate(ar,toadd):
            for i in range(len(ar)):
                for j in range(i+1,len(ar)):
                    if abs(ar[i][0] - ar[j][0]) ==abs(ar[i][1] - ar[j][1]) or ar[i][0]==ar[j][0]:
                        return 0
            if not toadd:return 1
            temp =[[ "." for i in range(n) ] for i in range(n)]
            for i in ar:
                temp[i[0]][i[1]] = "Q"
            z = ["".join(i ) for i in temp ]
            sol.append(z[:])

        def backtrack(col,ar):
            if len(ar) == n:
                validate(ar,1)
                return 
            for i in range(n):
                if not validate(ar,0): continue
                ar.append((i,col))
                backtrack(col+1,ar[:])
                ar.pop()
        
        backtrack(0,[])
        return sol