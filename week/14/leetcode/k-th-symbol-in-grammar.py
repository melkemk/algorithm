class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        odd = 0 
        k-=1
        while k:
            if k%2:odd+=1
            k//=2
            
        return  int( odd%2)
