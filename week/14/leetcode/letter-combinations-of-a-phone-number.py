class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.ans  = []
        di = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        def helper(idx,curr):
            if len(curr) ==len(digits):
                if not curr:return
                self.ans.append("".join(curr[:]))
                return
            if idx>=len(digits):return
            for i in range( len(di[int(digits[idx])]   )):
                curr.append(di[int(digits[idx])][i])
                helper(idx+1,curr)
                curr.pop()
                helper(idx+1,curr)
        helper(0,[])
        return self.ans


