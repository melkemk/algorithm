class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def rec( idx,j, curr):
            if sum(curr) == target:
                self.ans.append(tuple(sorted(curr[:])))
                return 
            if idx>=j:return
            for i in range(idx,j):
                if i>idx  and nums[i]==nums[i-1]:
                    # print(curr,i)
                    continue
                curr.append(nums[i])

                if sum(curr) >target:
                    curr.pop()
                    continue
                rec(i+1,j,curr)
                curr.pop()
        # if sum(nums) <target:return []
        rec(0,len(nums),[])
        return set(self.ans)