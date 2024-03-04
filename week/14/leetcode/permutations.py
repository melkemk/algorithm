class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def helper(partial):
            if len(partial)==len(nums):
                ans.append(partial[:])
                return
            for i in range(len(nums)):
                if nums[i] in partial:continue
                partial.append(nums[i])
                helper(partial)
                partial.pop()
        helper([])
        return ans
