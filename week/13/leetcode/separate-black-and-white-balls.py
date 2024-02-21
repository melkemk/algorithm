class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros ,ans = 0,0
        for i in reversed(s):
            if i =='0':
                zeros += 1
            else: 
                ans += zeros
        return ans