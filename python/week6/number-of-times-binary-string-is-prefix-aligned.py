class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        bits=[i+1 for i in range(len(flips))]
        leftcount=0
        maxi=0
        ans=0
        for j in flips:
            leftcount+=1
            maxi=max(j,maxi)
            if leftcount==maxi:ans+=1
        return ans