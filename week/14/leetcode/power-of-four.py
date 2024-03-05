class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def ispoweroffour(num):
            if num<=1:
                return num==1
            return ispoweroffour(num/4)
        return ispoweroffour(n)