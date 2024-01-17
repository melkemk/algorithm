class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        di=defaultdict(int)
        di[0]=1
        su=0
        ans=0
        for i in range(len(nums)):
            su+=nums[i]
            if su%k in di:
                ans+= di[su%k ]
            di[su%k]+=1

        return ans

            
