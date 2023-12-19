class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=s
        i=0
        kk=0
        while(i<len(s)):
            print(s[i:i+k],i ,kk)
            if len(s)-i<k:
                s = s[:i] + s[i::][::-1]
            else:
                s = s[:i] + s[i:i+k][::-1] + s[i+k:]
            kk+=2*k
            i=kk
        # i-=k
        # s = s[:i] + s[i:i+k][::-1] + s[i+k:]
        return s
            