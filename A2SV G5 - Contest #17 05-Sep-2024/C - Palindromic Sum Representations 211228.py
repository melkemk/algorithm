# Problem: C - Palindromic Sum Representations - https://codeforces.com/gym/524965/problem/C

from cmath import inf, sqrt
from collections import defaultdict
import sys

def yn(cond):
    if cond:return 'YES'
    return 'NO'
def ip(num=0):
    return list( map(int, sys.stdin.readline().strip().split())) if not num  else [int(i) for i in (list(sys.stdin.readline().strip()))]
mod = 10**9+7
coins = []

for i in range(1,40000):
    if str(i) ==str(i)[::-1]:coins.append(i)
ans = [0]*(40001)
ans[0] += 1 
for j in coins:
    for i in range(j,40000+1):
        ans[i] += (ans[i-j])
        ans[i]%=mod
    

def solve():
    n = ip()[0]
    print(ans[n])
    


T = 1
T = int(input())

for _ in range(T):
    solve()
        
        
            
        
        
        