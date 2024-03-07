class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        idx = {tuple(nums):i for i,nums in enumerate(intervals)}
        intervals.sort()
        ar = [-1]*len(intervals)
        t = [i for i,j in intervals]
        for j,i in enumerate(intervals):
            x = bisect_left(t,i[1])
            if x<len(intervals):
                ar[ idx[tuple(i)] ] =  idx[tuple(intervals[x])]
        return ar