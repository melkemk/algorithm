class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros,ones =  0 ,0
        zeropre ,onepre= [0]*len(s) ,[0]*len(s)
        for i,j in enumerate(s):
            if j =='0' :
                zeros += 1
                onepre[i] = ones
            else:
                zeropre[i] = zeros
                ones += 1

        zeropre = list(accumulate(zeropre))
        onepre  = list(accumulate(onepre))
        # zero = len(s) - 1-s[::-1].index('0')
        # one = len(s) - 1-s[::-1].index('1')
        zero,one=True,True
        ans =0 
        for i in range(len(s)):
            if  zero and one :
                if s[i]=='0' :
                    ans+= zeropre[i]
                else:
                    ans +=onepre[i]
            elif s[i] =='0':zero=True
            else: one =True

        return ans
        