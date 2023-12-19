class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        num=[i for i in range(1,n+1)]
        i,p=k-1,0
        while(len(num)!=1):
            print(num,i)
            num.pop(i)
            i+=k-1
            if i >=len(num):
                i=i%len(num)
        return num[0]