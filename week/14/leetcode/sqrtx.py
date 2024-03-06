class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        left=1
        right=int(x/2)
        middle=0
        while(left<=right):
            print(left,middle,right)
            middle= int((right+left)/2)
            if(((x>middle**2) and x<((middle+1)**2) )or x==middle**2):
                return middle
            elif(x>(middle**2)):
                left=middle+1
            else:
                right=middle-1
        return middle