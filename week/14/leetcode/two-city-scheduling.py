class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:x[0]-x[1])
        half,ans=len(costs)//2,0
        for i in range(half):
            ans+=costs[i][0]
            ans+=costs[half+i][1]
        return ans
