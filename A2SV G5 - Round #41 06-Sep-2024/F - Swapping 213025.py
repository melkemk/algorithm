# Problem: F - Swapping - https://codeforces.com/gym/544853/problem/D

from cmath import inf, sqrt
from collections import defaultdict
import sys

def yn(cond):
    if cond:return 'YES'
    return 'NO'
def ip(num=0):
    return list( map(int, sys.stdin.readline().strip().split())) if not num  else [int(i) for i in (list(sys.stdin.readline().strip()))]
def solve():
    n,x,m = ip()
    l,r = x,x
    for i in range(m):
        a,b = ip()
        if a<=l<=b or a<=r<=b:
            l  = min(l,a)
            r = max(r,b)
    print(r-l+1)
            
        
    


T = 1
T = int(input())

for _ in range(T):
    solve()
        
        
            
        
        
        