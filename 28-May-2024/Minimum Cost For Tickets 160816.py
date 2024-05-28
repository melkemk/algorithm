# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(i,covered):
            if i==len(days):return 0 
            if days[i] <=covered:
                return dp(i+1,covered)
            else :
                _min = min(dp(i+1,days[i]  )+ costs[0] ,dp(i+1,days[i]+ 6)+costs[1],dp(i+1,days[i]+29) + costs[2])
                return _min
        return dp(0,0)
        
