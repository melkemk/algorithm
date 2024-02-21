class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        close,open,ans = 0,0,0
        
        for j,i in enumerate(s):
            if i==')':
                close +=1
                if close >open :
                    ans += (close -open )
                    open = close 
            else:
                open += 1
                
        return ans +abs(close-open)