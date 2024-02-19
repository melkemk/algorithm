class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        odd = False
        ans = 0
        for i in counter:
            if not counter[i] % 2:
                ans += counter[i]
            else:
                 odd = True
                 ans += counter[i]-1
        if  odd: return ans+1 
        return ans