class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        a=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and not (i*j)%k :
                    a+=1
                    
        return (a)