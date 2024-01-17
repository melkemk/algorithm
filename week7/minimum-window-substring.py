class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left,right=0,0
        counter_t=Counter(t)
        counter_s=defaultdict(int)
        _min=inf
        word=[0,0]
        while left<len(s) and right<len(s):
            while(right<len(s) and  not all(counter_s[t] >=counter_t[t] for t in counter_t  )):
                counter_s[s[right]]+=1
                right+=1
            while(left<len(s) and all(counter_s[t] >=counter_t[t] for t in counter_t  )):
                if _min>right-left+1:
                    _min=right-left+1
                    word=[left,right]
                counter_s[s[left]]-=1
                left+=1
        return s[word[0]:word[1]]
            