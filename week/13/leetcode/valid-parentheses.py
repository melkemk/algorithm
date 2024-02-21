class Solution:
    def isValid(self, s: str) -> bool:
        a= {'}': '{', ')': '(', ']': '['}
        pare = {v: k for k, v in a.items()}

        sa=[]
        for i in s:
            if i  in pare:
                sa.append(pare[i])
            else:
                if(len(sa)<1):return False
                if sa.pop()!=i:return False
        print(sa)
        return len(sa)==0

