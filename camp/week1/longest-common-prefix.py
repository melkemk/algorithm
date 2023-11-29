class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = min(len(ele) for ele in strs)
        str=""
        i=0
        while(i<res):
            s=strs[0][i]
            fa=False
            for j in range(1,len(strs)):
                if(strs[j][i]!=s):
                    fa=True
            if(not fa):
                str+=s
            else:
                break
            i+=1
        return str
                    
