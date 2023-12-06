class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=list()
        tri=len(nums)//3
        for i in nums:
            if(nums.count(i)>tri):
                ans.append(i)
        return set(ans)