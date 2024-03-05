class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def rec(i,j,partial):
            if i>=j:return
            partial.append(nums[i])
            ans.add(tuple(partial[:]))
            rec(i+1,j,partial)
            partial.pop()
            rec(i+1,j,partial)
        rec(0,len(nums),[])
        ans.add(tuple([]))
        return ans