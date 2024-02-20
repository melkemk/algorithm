class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        temp=target
        ans=0
        while maxDoubles and temp>1:
            if temp//2 *2!= temp:ans+=1
            maxDoubles-=1
            temp//=2
            ans+=1
        print(temp,ans)
        ans+=temp-1
        return ans