class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        tempsum,left,right=0,0,len(cardPoints)-1
        win=sum(cardPoints[:k])
        _max=win
        j=len(cardPoints)-1
        i=0
        print(win)
        while(j>len(cardPoints)-k-1):
            win-=cardPoints[k-i-1]
            win+=cardPoints[j]
            print(cardPoints[j])
            _max=max(_max,win)
            j-=1
            i+=1
        return _max