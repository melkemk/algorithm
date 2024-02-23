class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(nums)
        for j,i in enumerate(nums):
            while stack and stack[-1][1] <i:
                t,num = stack.pop()
                ans[t] = j-t
            stack.append((j,i))
       
        return ans