class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        _max = 0 
        i = 0 
        ans = []
        index ={}
        for i,j in enumerate(s):
            index[j] = i
        i = 0 
        while i<len(s):
            _max =  max(index[s[i]],_max)
            leng = 0
            while i!=_max:
                i += 1
                leng += 1
                _max =  max(index[s[i]],_max)
            ans.append(leng+1)
            i += 1
        return ans

