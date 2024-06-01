# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

from cmath import inf, sqrt
from collections import defaultdict
import sys

def yn(cond):
    if cond:return 'YES'
    return 'NO'
def ip(num=0):
    return list( map(int, sys.stdin.readline().strip().split())) if not num  else [int(i) for i in (list(sys.stdin.readline().strip()))]
def solve():
    # pass
    m,s = ip()
    if m==1 and s==0:
        print(0,0)
        return
    mm =  m
    ss = s
    _max = []
    for i in range(m):
        _max.append(min(9,s))
        s = max(s-9,0)
    _min = []
    s = ss-1
    
    for i in range(m-1):
        _min.append(min(9,s))
        s = max(s-9,0) 
    _min = [1] + _min[::-1]
    if 9*m < ss or ss==0:
        print(-1,-1)
    else:
        if s :_min[0] +=s
        print("".join( str(i) for i in  _min),"".join( str(i) for i in  _max))
     
        
        
     
    
        
        
        
    


T = 1
# T = int(input())

for _ in range(T):
    solve()
        
        
            
        
        
        