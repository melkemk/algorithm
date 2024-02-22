class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        di ={i:-1 for i in nums}
        ans = [-1]*len(nums)
        for j,i in enumerate(nums):
            while stack and stack[-1][1] <i:
                t,num = stack.pop()
                print(num)
                ans[t] = i
            stack.append((j,i))
        if stack:
            for j,i in enumerate(nums):
                while stack and stack[-1][1] <i:
                    t,num = stack.pop()
                    ans[t] = i 
        return ans