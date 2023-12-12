class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(100):
            s=str(n)
            sum=0
            for i in range(len(s)):
                sum+=int(s[i])**2
            n=sum
            if n==1:return True
        return False
            