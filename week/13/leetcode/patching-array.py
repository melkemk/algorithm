class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        target , patch , i =1,0,0
        while target <= n:
            if i<len(nums)  and nums[i]<=target :
                target += nums[i]
                i += 1
            else:
                target*=2
                patch += 1
        return patch 
