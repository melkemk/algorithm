class Solution:
    def myPow(self, x: float, n: int) -> float:
        def myPow(x,n):
            if n ==1.0 :return x
            if n == 0 :return 1
            if n%2:
                ans = myPow(x,(n-1)/2)
                return ans*ans*x
            ans = myPow(x,(n)/2)
            return ans *ans
        return 1/(myPow(x,n*-1)) if n<0 else myPow(x,n)