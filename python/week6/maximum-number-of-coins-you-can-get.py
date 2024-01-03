class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        num=0
        i=len(piles)-2
        while(i>=len(piles)//3):
            num+=piles[i]
            print(i)
            print(num,piles[i])
            i-=2
        return num