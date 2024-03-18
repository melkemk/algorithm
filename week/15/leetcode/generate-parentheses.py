class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = set()
        def validate(ar):
            stack = []
            for i in ar:
                if i=='(':
                    stack.append(i)
                else: 
                    if stack:stack.pop()
                    else:return 0 
            return len(stack)==0

        def backtrack(ar):
            if len(ar)==2*n:
                self.ans.add("".join(ar))
                return
            ar.append('(')
            backtrack(ar)
            ar.pop()
            ar.append(')')
            backtrack(ar)
            ar.pop()
        backtrack([])
        ans = list(filter(validate,self.ans))
        return ans

            

