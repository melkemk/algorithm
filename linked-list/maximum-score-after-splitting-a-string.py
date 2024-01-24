class Solution:
    def maxScore(self, s: str) -> int:
        maxi=0
        # count_one=s.count("1")
        # count_zero=s.count("0")
        for i in range(len(s)-1):
            maxi=max(s[0:i+1].count("0")+s[i+1::].count("1"),maxi)
        return maxi
