class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        looses=set()
        win=set()
        onlyones={}
        for i,j in matches:
            looses.add(j)
            win.add(i)
            onlyones[j] = onlyones.get(j,0)+1
        ans=[sorted(list(win  -looses)),sorted( [i for i in onlyones if onlyones[i]==1] )]
        return ans

            
