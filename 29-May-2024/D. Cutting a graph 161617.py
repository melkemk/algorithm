# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

from cmath import inf, sqrt
from collections import defaultdict
import sys

def yn(cond):
    if cond:return 'YES'
    return 'NO'
def ip(num=0):
    return list( map(int, sys.stdin.readline().strip().split())) if not num  else [int(i) for i in (list(sys.stdin.readline().strip()))]
class UnionFind:
    def __init__(self, total):
        self.parent = {i+1:i+1 for i in range(total)}
        self.size = [1] * (total+1)
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    
    def union(self, x , y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX == parentY:return 
        if self.size[parentX]>self.size[parentY]: 
            self.size[parentX] += self.size[parentY]
            self.parent[parentY] = parentX
        else:
            self.size[parentY] += self.size[parentX] 
            self.parent[parentX] = parentY  
    def cut(self,x,y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != x:
            self.parent[x] = x
        elif parentY != y:
            self.parent[y] = y

        
def solve():
    n,m,k = ip()
    un = UnionFind(n)
    for _ in range(m):
        x,y = ip()
        # un.union(x,y)
    words = []
    for _ in range(k):
        word = input().split()
        words.append(word)
    ans  = []
    for word in reversed(words):
        a,b =  map(int,word[1:])
        if word[0]=='cut':
            un.union(a,b)
        else:
            ans.append( yn(un.find(a) ==un.find(b)))
    for i in reversed(ans):print(i)
            
            
    


# T = int(input())
T = 1

for _ in range(T):
    solve()
   
                