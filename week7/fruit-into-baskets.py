class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        _max,left=0,0
        di={}
        for right in range(len(fruits)):
            di[fruits[right]]=di.get(fruits[right],0)+1
            while left<len(fruits) and len(di)>2:
                _max=max(_max,right-left)
                if di[fruits[left]]==1:
                    di.pop(fruits[left])
                else:di[fruits[left]]-=1
                left+=1
            _max=max(_max,right-left+1)
        return _max