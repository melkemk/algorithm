# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        _sum = sum(nums)
        if _sum%k:return 0
        print(_sum)
        @cache
        def dp(par,di):
            if len(di) ==len(nums) :return par ==0 
            if par == 0 :
                return dp(_sum//k,di)
            _max = 0 
            for i in range(len(nums)):
                if  par-nums[i] >=0:
                    if i not in di:
                        _max += (dp(par-nums[i],tuple(set(di)| {i})))
            return _max
        return dp(_sum//k,tuple())
