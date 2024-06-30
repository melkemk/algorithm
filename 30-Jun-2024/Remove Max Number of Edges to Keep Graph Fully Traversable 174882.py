# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self, total):
        self.parent = {i:i for i in range(1,1+total)}
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def join(self, x , y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX == parentY:return 
        if parentX>parentY: 
            self.parent[parentY] = parentX 

        else:
            self.parent[parentX] = parentY

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse = True)
        ans = 0
        dsu =  [UnionFind(n), UnionFind(n)]
        for i,j,k in edges:
            if dsu[0].find(j)==dsu[0].find(k) and dsu[1].find(j)==dsu[1].find(k)  :
                ans += 1  
                continue
            if i==3:
                dsu[1].join(j,k)
                dsu[0].join(j,k)
            else:
                if (i==1 and  dsu[0].find(j)==dsu[0].find(k)) or (i==2 and dsu[1].find(j)==dsu[1].find(k) ):
                    ans += 1 
                dsu[i-1].join(j,k)
        for i in range(n):
            if dsu[0].find(i+1) !=dsu[0].find(1) or dsu[1].find(i+1) !=dsu[1].find(1):
                return -1 
        return ans 


