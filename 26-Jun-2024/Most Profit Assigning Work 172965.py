# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dprofit  = [[difficulty[i],profit[i]] for i in range(len(profit))]
        dprofit.sort()
        for i in range(1,len(profit)):
            dprofit[i][1] = max(dprofit[i-1][1],dprofit[i][1])
        ans =  0 
        diff = [i for i,j in dprofit]
        for i in range(len(worker)):
            inx = bisect_right(diff,worker[i])
            if inx:
                ans += dprofit[inx-1][1]
        return ans 