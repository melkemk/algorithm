class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        counter=defaultdict(int)
        _max=0
        for right in range(len(s)):
            counter[s[right]]+=1
            while(sum(counter[i] for i in counter)-max(counter[i] for i in counter)>k):
                counter[s[left]]-=1
                left+=1
            _max=max(_max,right-left+1)
        return _max
            