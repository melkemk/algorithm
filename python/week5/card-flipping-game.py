class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        possible=set(sorted(set(fronts) | set(backs)))
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                possible.discard(fronts[i])
        return next(iter(possible)) if possible else 0
        


