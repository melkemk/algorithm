# Problem: E - XOR Fan - https://codeforces.com/gym/522079/problem/E

from cmath import inf, sqrt
from collections import defaultdict
import sys

def yn(cond):
    if cond:return 'YES'
    return 'NO'
def ip(num=0):
    return list( map(int, sys.stdin.readline().strip().split())) if not num  else [int(i) for i in (list(sys.stdin.readline().strip()))]

def solve():
    n = ip()[0]
    ar = ip()
    bina = ip(1)
    q = ip()[0]
    pref  = [0]*(n+1)
    one,zero  =0,0
    for i in range(1,n+1):
        pref[i] = pref[i-1]^ar[i-1]
        if bina[i-1]:one^=ar[i-1]
        else:zero^=ar[i-1]
    for i in range(q):
        query = ip()
        if len(query)==2:
            print(one if query[1]==1 else zero,end = " ")
        else:
            l,r = query[1:]
            x = pref[r]^(pref[l-1])
            one^=x
            zero^=x
    print()
            
            
    


T = int(input())
# T = 1

for _ in range(T):
    solve()
        
        
            
        
        
        