# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones = [tuple(stone) for stone in stones]
        parent = {i:i for i in stones}
        def find(i):
            if parent[i] == i:return i 
            parent[i] = find(parent[parent[i]])
            return parent[i]
        def unite(x,y):
            xp,yp = find(x),find(y)
            if xp==yp:return 
            parent[yp] = xp 
        
        for i in range(len(stones)):
            for j in range(i+1,len(stones)):
                if stones[i][0] ==  stones[j][0] or stones[i][1] ==stones[j][1]:
                    unite(stones[i],stones[j])
        ans = set()
        print(parent)
        for i in range(len(stones)):
            ans.add(find(stones[i]))
        return len(stones)-  len(ans)