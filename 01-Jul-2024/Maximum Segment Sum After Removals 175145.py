# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class UnionFind:
    def __init__(self, total,nums):
        self.parent = {i:i for i in range(total)}
        self.size = [nums[i]  for i in range((total))] 
        print(total,self.parent)
    
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
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        
        dsu = UnionFind(len(nums),nums)
        _set = set()
        ans =[0]
        _max = 0 
        for i in range(len(nums)-1,-1,-1):
            i = removeQueries[i]
            if i+1 in _set: 
                dsu.union(i+1,i)
            if i-1 in _set:
                dsu.union(i-1,i)
            ans.append(max(_max,dsu.size[dsu.find(i)]))
            _set.add(i) 
            _max = max(_max,dsu.size[dsu.find(i)])
        return ans[:-1][::-1]

