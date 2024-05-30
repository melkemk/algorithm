# Problem: Turtle vs. Rabbit Race: Optimal Trainings - https://codeforces.com/contest/1933/problem/E

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
    n = ip()[0]
    ar = ip()
    pre = [0] +list( accumulate(ar))
    q = ip()[0]
    def f(l,m,u):
        ans = pre[m]- pre[l-1]
        x = (ans)*(ans-1)//2
        return ans*u-x
    # for i in range(1,n+1):
    #     print(f(1,i,8))
    # print()
    
        
    for _ in range(q):
        l,u = ip()
        
        low = l
        high = len(ar) 
        ans_index = None 

        while low <= high:
            
            p1 = low + (high - low) // 3
            p2 = high - (high - low) // 3
            # print(f(l,p1,u) , f(l,p2,u),p1,p2)
            if f(l,p1,u) < f(l,p2,u):
                ans_index = p2
                low = p1 + 1
            else:
                ans_index = p1
                high = p2 - 1
        print(ans_index,end=" ")
    print()


        
        
    


T = 1
T = int(input())

for _ in range(T):
    solve()
        
        
            
        
        
        