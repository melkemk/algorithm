from cmath import inf
import sys


num = int(int(sys.stdin.readline().strip()))
distance=list((map(int, sys.stdin.readline().strip().split()  )))
speed=list((map(int, sys.stdin.readline().strip().split()  )))



def mainfunc():
    def left(mid):
        
        _max =-inf
        for i in range(len(distance)):
            _max = max(_max,distance[i] -(speed[i]*mid))
        return max(_max,0)
    

    def right(mid):
        _min =inf
        for i in range(len(distance)):
            _min = min(_min,distance[i] +(speed[i]*mid))
        return _min



    low  ,high = 0,max(distance)+min(distance)
    while high-low >=pow(10,-6):
        mid = low + (high - low)/2
        if left(mid)<right(mid):
            high = mid - 10**-7
        elif left(mid)>right(mid):
            low = mid+ 10**-7
        else:return mid
        
    return low
print(mainfunc())