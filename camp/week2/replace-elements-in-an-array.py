class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num={n:i for i,n in enumerate(nums)}
        for i,j in operations:
            nums[num[i]]=j
            num[j]=num[i]
        return nums