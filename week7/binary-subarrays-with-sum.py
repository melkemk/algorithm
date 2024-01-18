class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre=0
        t=defaultdict(int)
        t[0]=1
        ans=0
        for i in nums:
            pre+=i
            if(pre-goal in t):
                ans+=t[pre-goal]
            t[pre]+=1
        return ans