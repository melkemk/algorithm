class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ans = [-1]*len(nums)
        stack = []
        prevmin = [inf]*len(nums)
        _min = nums[0]
        for i in range(1,len(nums)):
            prevmin[i] = _min
            _min = min(_min,nums[i])

        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] <nums[i] :
                temp = stack.pop()
                ans[temp] = i
            stack.append(i)
        print(ans,prevmin)
        for i in range(2,len(nums)):
            if ans[i] != -1:
                if prevmin[ans[i]] < nums[i]:
                    return 1
