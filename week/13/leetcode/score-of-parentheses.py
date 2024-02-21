class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        nums=[]
        maxa=0
        for i in s:
            if(i=='('):
                nums.append(maxa)
                maxa=0
            else:
                maxa=max(1,2*maxa)+nums.pop()
        return maxa