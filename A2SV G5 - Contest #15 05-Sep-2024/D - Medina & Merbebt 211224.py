# Problem: D - Medina & Merbebt - https://codeforces.com/gym/522079/problem/D

from collections import defaultdict
import sys

def yn(cond):
    if cond:
        return 'YES'
    return 'NO'

def ip(num=0):
    return list(map(int, sys.stdin.readline().strip().split())) if not num else [int(i) for i in (list(sys.stdin.readline().strip()))]

def solve():
    n = ip()[0]
    ar = ip()
    tt = ar[:]
    q = ip()[0]


    total = [0] * 31
    prefix = [[0] * 31]
    for i in range(n):
        arr = list(map(int, bin(ar[i])[2:].zfill(31)))
        for j in range(31):
            total[j] += arr[j]
        prefix.append(total[:])

    def helper(l, m):
        length = m-l+1
        l, m = prefix[l - 1], prefix[m]
        ans = [0] * 31
        for i in range(31):
            ans[i] = 1 if m[i] - l[i] ==length else 0
        return int("".join(str(i) for i in ans), 2)
    ans_list = []
    for _ in range(q):
        l, k = ip()
        ll = l 
        r =  n
        if tt[l-1] < k:
            print(-1,end=" ")
            continue
        while l <= r:
            mid = (l + r) // 2
            if helper(ll, mid) >= k:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        print(r,end=" "  )
    print()


T = int(input())

for _ in range(T):
    solve()