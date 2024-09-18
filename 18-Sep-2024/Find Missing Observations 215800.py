# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        t = len(rolls)+n 
        _sum = sum(rolls) 
        free = t*mean-_sum 
        if free>(6)*n or free<n:return []
        ar = []
        i = 0 
        avg = free//n 
        ar = [avg]*n
        x = free-avg*n
        for i in range(x):
            ar[i]+=1 
        return ar
