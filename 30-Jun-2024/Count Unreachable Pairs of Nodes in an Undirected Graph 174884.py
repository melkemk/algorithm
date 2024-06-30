# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class UnionFind:
    def __init__(self, total):
        self.parent = {i:i for i in range(total)}
        self.size = [1] * (total)
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    
    def union(self, x , y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX == parentY:return 
        if parentX>parentY: 
            self.size[parentX] += self.size[parentY]
            self.parent[parentY] = parentX

        else:
            self.size[parentY] += self.size[parentX] 
            self.parent[parentX] = parentY  

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        dsu,ans = UnionFind(n),0
        for i,j in edges :
            dsu.union(i,j)
        for i in range(n):
            ans += (n-(dsu.size[dsu.find(i)]))
        return ans//2