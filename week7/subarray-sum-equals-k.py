class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre=0
        t=defaultdict(int)
        t[0]=1
        ans=0
        for i in nums:
            pre+=i
            if(pre-k in t):
                ans+=t[pre-k]
            t[pre]+=1
        return ans
