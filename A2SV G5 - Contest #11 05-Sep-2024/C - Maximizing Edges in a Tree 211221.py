# Problem: C - Maximizing Edges in a Tree - https://codeforces.com/gym/515998/problem/C

from collections import defaultdict
import sys

def ip(num=0):
    return list( map(int, sys.stdin.readline().strip().split())) if not num  else [int(i) for i in (list(sys.stdin.readline().strip()))]

def solve():
    n = ip()[0]
    di = defaultdict(list)
    bipartitie  = defaultdict(bool)

    for t in range(n-1):
        a,b = ip()
        di[a].append(b)
        di[b].append(a)

    t = [True]
    x = 0 
    visited = set()
    for r in di:
        if r not in visited:
            stack = [(r,True)]
            while  stack:
                x,j  = stack.pop()
                bipartitie[x] = j
                for i in di[x]:
                    if i not in visited:
                        stack.append((i,not j ))
                        t.append(not j )
                        visited.add(i)
                        x+=1
    
    count = 0 
    count0 = 0 
    for i in di:
        if bipartitie[i]:count+=1
        else: count0+=1
    print( count *count0 -n +1 )
    
    


# T = int(input())
T = 1

for _ in range(T):
    solve()
        
        
            
        
        
        