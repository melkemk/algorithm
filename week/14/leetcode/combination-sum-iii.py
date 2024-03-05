class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        self.ans = []
        self.nums = [i for i in range(9,0,-1)]
        def rec( idx,j, curr):
            if sum(curr) == target and k ==len(curr):
                self.ans.append(tuple(sorted(curr[:])))
                return 
            if idx>=j:return
            for i in range(idx,j):
                if i>0  and self.nums[i]==self.nums[i-1]:
                    print(curr,i)
                    continue
                curr.append(self.nums[i])
                if sum(curr) >target:
                    curr.pop()
                    continue
                rec(i+1,j,curr)
                curr.pop()
        rec(0,len(self.nums),[])
        return set(self.ans)