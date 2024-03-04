class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def rec( idx,j, curr):
            if idx>=j:return
            if sum(curr) == target:
                self.ans.append(curr[:])
                return 
            for i in range(idx,j):
                curr.append(nums[i])
                if sum(curr) >target:
                    curr.pop()
                    continue
                rec(i,j,curr)
                curr.pop()
        rec(0,len(nums),[])
        return self.ans