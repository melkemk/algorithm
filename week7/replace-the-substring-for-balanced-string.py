class Solution:
    def balancedString(self, s: str) -> int:
      c=Counter(s)
      left=0
      _min=len(s)
      for i in range(len(s)):
          c[s[i]]-=1
          while(left<len(s) and all(c[j]<=len(s)/4 for j in c)):
              _min=min(_min,i-left+1)
              c[s[left]]+=1
              left+=1
      return _min