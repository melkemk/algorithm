class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        def rec(i,j,partial):
            ans.append(tuple(sorted(partial)))
            if i>=j:return

            for i in range(i,j):
                partial.append(nums[i])
                rec(i+1,j,partial)
                partial.pop()
        rec(0,len(nums),[])
        return set(ans)