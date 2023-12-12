class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1
        dic=defaultdict(int)
        for i,j in enumerate(nums):
            if(j in dic):
                return [dic[j],i]
            a=target-j
            dic[a]=i
