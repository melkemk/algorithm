# Problem: Two Sum - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=defaultdict(int)
        for i,j in enumerate(nums):
            if(j in dic):
                return [dic[j],i]
            a=target-j
            dic[a]=i
