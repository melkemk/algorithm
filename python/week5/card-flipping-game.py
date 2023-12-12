class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        i=len(fronts)-1
        possible=set(sorted(set(fronts) | set(backs)))
        while(i>=0):
            if fronts[i]==backs[i]:
                possible.discard(fronts[i])
            i-=1
        if len(possible):return next(iter(possible))
        return 0


