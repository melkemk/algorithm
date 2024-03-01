class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        _sum = sum(nums) 

        def rec(l,r,ord):
            if l> r:
                    return 0
            if ord:
                return min(0-nums[l]+ rec(l+1,r, not ord ), 0-nums[r] + rec(l,r-1,not ord))

            return max(nums[l]+ rec(l+1,r, not ord ), nums[r] + rec(l,r-1,not ord))
        ans =rec(0,len(nums)-1,0)

        return ans>=0
