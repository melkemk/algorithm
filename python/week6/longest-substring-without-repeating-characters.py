class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last=0
        di={}
        col=[]
        for i in range(len(s)):
            print(s[i] in s[last:i],last)
            if s[i] in s[last:i] :
                col.append(i-last)
                last=di[s[i]]+1
            di[s[i]]=i
        col.append(len(s)-last)
        return max(col)
