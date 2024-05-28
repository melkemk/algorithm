# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class UnionFind:
    def __init__(self, total):
        self.parent = {i:i for i in range(total)}
        self.size = [1] * (total+1)
        self.ans = []
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
 
    
    def union(self, x , y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX == parentY:return 
        if parentX<parentY: 
            self.parent[parentY] = parentX
        else:
            self.parent[parentX] = parentY 
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x:x[2])
        union = UnionFind(n)
        union.union(0,firstPerson)
        i = 0 
        ans = []
        while i <len( meetings):
            time = meetings[i][2]
            temp = []
            while i<len(meetings) and meetings[i][2]==time:
                x,y,z = meetings[i]
                union.union(x,y)
                temp.append(x)
                temp.append(y)
                i += 1 
            for ii in temp:
                if union.find(ii)!=0:union.parent[ii] = ii
        ans = [ ]
        for i in range(n):
            if union.find(i) ==0:ans.append(i)
 
        return ans