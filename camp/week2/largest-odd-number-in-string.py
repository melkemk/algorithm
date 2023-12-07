class Solution:
    def largestOddNumber(self, num: str) -> str:
        lastodd=None
        for j,i in enumerate(num):
            if int(i)%2==1:
                lastodd=j
        if lastodd or lastodd==0: return (num[:lastodd+1])
        return ""