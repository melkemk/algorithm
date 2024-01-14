class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left,_min=0,inf
        leng=k
        t=0
        for right in range(len(blocks)):
            if blocks[right]=='W':
                t+=1
            if right-left==leng-1:
                _min=min(_min,t)
                if blocks[left]=='W':
                    t-=1
                left+=1
        print(_min)
        return _min if _min!=inf else 0