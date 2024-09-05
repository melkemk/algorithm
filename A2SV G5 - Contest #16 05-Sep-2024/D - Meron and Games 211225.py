# Problem: D - Meron and Games - https://codeforces.com/gym/523525/problem/D

from bisect import bisect_left
from math import floor, inf, sqrt
from collections import Counter, defaultdict
import sys

def yn(cond):
    if cond:return 'YES'
    return 'NO'
def ip(num=0):
    return list( map(int, sys.stdin.readline().strip().split())) if not num  else [int(i) for i in (list(sys.stdin.readline().strip()))]
def solve():
    n = ip()[0]
    counter = Counter(ip())
    dp = [counter[i]*i for i in range(10**5+1)]
    # print(dp)
    if len(dp)>2:dp[2]+= dp[0]
    for i in range(3,len(dp)):
        dp[i]= max(dp[i-2],dp[i-3])+dp[i]
    # print(dp)
    print(max(dp))
    
    
    
            
        
        
    


T = 1
# T = int(input())

for _ in range(T):
    solve()
        
        
            
        
        
        