class Solution:
    def countGoodNumbers(self, a: int) -> int:
        num = a/2
        def countGoodNumber(m,n):
            if n ==1.0:return m
            elif n%2 :
                ans = countGoodNumber(m,(n-1)/2)
                return (ans * ans * m)%((10**9)+7)
            else:
                ans = countGoodNumber(m,n/2)
                return (ans * ans )%((10**9)+7)
        return ((countGoodNumber(4,floor(num)) if floor(num) else 1) * countGoodNumber(5,ceil(num)))%( 10**9 + 7)
