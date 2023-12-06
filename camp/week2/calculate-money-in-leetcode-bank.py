class Solution:
    def totalMoney(self, n: int) -> int:
        monday=-1
        i=0
        sum=0
        x=0
        for j in range(n//7):
            monday+=1
            x=monday
            for k in range(7):
                i+=1
                x+=1
                sum+=x
                # print(x,sum)
        monday+=1
        x=monday
        
        for j in range(i+1,n+1):
            x+=1
            sum+=x
            print(x,sum,j)
        return sum
