from collections import defaultdict
for _ in range(int(input())):
    input()
    a=input()
    ar=[0]
    for i in range(len(a)):
       ar.append(int(a[i])) 
    _sum=0
    for i in range(len(ar)):
        _sum+=ar[i]
        ar[i]=_sum
    total=0 
    di=defaultdict(int)
    for i in range(len(ar)):
        if ar[i]-i-1 in di:
            total+=di[ar[i]-i-1]
        di[ar[i]-i-1]+=1
    print(total)