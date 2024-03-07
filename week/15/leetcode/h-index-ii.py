class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        _min = -inf
        for i in range(len(citations)-1,-1,-1):
            x = len(citations)- bisect_left(citations, citations[i])
            _min = max(_min, min(x ,citations[i]) )
        return _min 