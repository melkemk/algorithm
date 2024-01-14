class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        _min=float("inf")
        di={}
        for right in range(len(cards)):
            if cards[right] in di:
                _min=min(right-di[cards[right]]+1,_min)
            di[cards[right]]=right
        return _min if _min!=float("inf") else -1