class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key =lambda x:x[1])
        last = points[0][1]
        ans = 1
        for point in points:
            if point[0] >last:
                last = point[1]
                ans += 1
        return ans