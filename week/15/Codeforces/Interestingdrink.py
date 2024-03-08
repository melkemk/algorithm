from collections import defaultdict
import copy


total = int(input())
shop = list(map(int,input().split()))
shop.sort()
moneys = []
for _ in range(int(input())):
    moneys.append(int(input()))
ans = defaultdict(int)

moneycopy = copy.deepcopy(moneys)

moneys.sort()
temp,i  = 0,0
for money in moneys:
    while i<len(shop) and money>= shop[i]:
        temp +=1
        i +=1
    ans[money] = temp
for i in moneycopy:
    print(ans[i])