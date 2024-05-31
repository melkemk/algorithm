# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

from cmath import inf, sqrt
from collections import defaultdict
import sys

def yn(cond):
    if cond:return 'YES'
    return 'NO'
def ip(num=0):
    return list( map(int, sys.stdin.readline().strip().split())) if not num  else [int(i) for i in (list(sys.stdin.readline().strip()))]

def solve():
    n = (int(input()))
    num = bin(n)
    if n==1:return 3
    num = num[2:]
    num = list(num)
    i = n.bit_length()-1
    while i>-1:
        if num[i] ==  '1' and i ==0:
            num[-1] = '1'
            return int(''.join(num),2)
        if num[i] ==  '1':
            return int(''.join(num[i:]),2)
        i -=1
            
        
            
        
        
    


T = int(input())
# T = 1

for _ in range(T):
    print(solve())
        
        
            
        
        
        