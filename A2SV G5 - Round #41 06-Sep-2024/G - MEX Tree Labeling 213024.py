# Problem: G - MEX Tree Labeling - https://codeforces.com/gym/544853/problem/E

from cmath import inf, sqrt
from collections import defaultdict, deque
import sys

def yn(cond):
    if cond:return 'YES'
    return 'NO'
def ip(num=0):
    return list( map(int, sys.stdin.readline().strip().split())) if not num  else [int(i) for i in (list(sys.stdin.readline().strip()))]
def solve():
    n   = ip()[0]
    graph = defaultdict(list)
    x = [0 for i in range(n+1)]
    tt = []
    for i in range(n-1):
        a,b = ip()
        tt.append((a,b))
        graph[a].append(b)
        graph[b].append(a)
        x[a]+=1
        x[b]+=1
    z  = x.index(max(x))
    queue = deque([z])  
    n = 0
    ans = defaultdict(int) 
    visited = set()
    while queue:
        for _ in range(len(queue)):
            
            last = queue.popleft()
            visited.add(last)
            
            for  i in graph[last]:
                if i not in visited:
                    ans[(i,last)] = n 
                    ans[(last,i)] = n  
                    n+=1
                    queue.append(i)
    for i in tt:
        print(ans[i])
    
        


T = 1
# T = int(input())

for _ in range(T):
    solve()
        
        
            
        
        
        