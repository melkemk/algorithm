# Problem: Maximum Number of Zeros - https://codeforces.com/gym/514644/problem/D

from collections import defaultdict
from math import gcd
import sys


def ip():
    return list( map(int, sys.stdin.readline().strip().split()))
n = ip()[0]
a = ip()
b = ip()
ar = defaultdict(int)
anss = 0  
for i in range(n):
    if a[i]==0:
        if b[i]==0:anss += 1
    else: 
        _gcd = gcd(abs(b[i]),abs(a[i]))
        minus = 1
        if a[i]<0 and b[i]<0:minus=1
        elif  a[i]<0 or b[i]<0 :minus=-1
        ar[(minus*abs(b[i])//_gcd,abs(a[i])//_gcd)]+=1
ans = [0,0]
for i in ar:
    if ar[i]>ans[1]:
        ans = [i,ar[i]]
        
print(ans[1]+anss)
        
    