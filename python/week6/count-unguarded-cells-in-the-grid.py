class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat=[[1 for i in range(n) ] for i in range(m)]
        ans=set()
        wall={(i,j) for i,j in walls}
        guard={(i,j) for i,j in guards}
        for i,j in guards:#right
            for c in range(j+1,n):
                if  (i,c)  in wall or (i,c) in guard :break
                ans.add((i,c))
            for c in range(j-1,-1,-1):
                if  (i,c)  in wall or (i,c) in guard :break
                ans.add((i,c))
            for c in range(i-1,-1,-1) :
                if  (c,j) in wall or (c,j) in guard:break
                ans.add((c,j))
            for c in range(i+1,m) :
                if  (c,j) in wall or (c,j) in guard:break
                ans.add((c,j))
        # print(a?
        return n*m- (len(guards)+len(walls)+len(ans))