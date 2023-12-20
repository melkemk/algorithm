class Solution:
    def reverseString(self, s: List[str]) -> None:
       i=len(s)//2
       leng=len(s)-1
       for x in range(i):
         s[x],s[leng-x]= s[leng-x],s[x]