class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        stack = []
        ans = [len(nums)]*len(nums)
        ans2 = [-1]*len(nums)
        for i in range(len(nums)):
            while stack and stack[-1][0] > nums[i]:
                num , inx = stack.pop()
                ans[inx] =i
            stack.append((nums[i],i))
        stack = []
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1][1] >nums[i]:
                t,num = stack.pop()
                ans2[t] = i
            stack.append([i,nums[i]])
        _max = 0 
        for i in range(len(nums)):
            _max =  max((ans[i] - ans2[i] - 1) * nums[i],_max)
        return _max