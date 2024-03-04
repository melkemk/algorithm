class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans  = []
        def rec( i,j, curr):
            if len(curr)==k:
                ans.append(curr[:])
                return 
            for i in range(i,j):
                curr.append(i)
                rec(i+1,j,curr)
                curr.pop()
        rec(1,n+1,[])
        return ans
