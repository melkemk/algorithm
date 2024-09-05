# Problem: E - Consecutive Subarrays - https://codeforces.com/gym/523525/problem/E

from cmath import inf, sqrt
from collections import defaultdict
from itertools import accumulate
import sys

def yn(cond):
    if cond:return 'YES'
    return 'NO'
def ip(num=0):
    return list( map(int, sys.stdin.readline().strip().split())) if not num  else [int(i) for i in (list(sys.stdin.readline().strip()))]
def solve():
    n,k = ip()
    ar = ip()
    pre = list(accumulate(ar))
    pre = list(pre[::-1])
    ans = k*pre[0]
    x =sorted( pre[1:])
    ans -=sum (x[0:k-1])
    print(ans)
    
    


T = 1
# T = int(input())

for _ in range(T):
    solve()
        
        
            
        
        
        