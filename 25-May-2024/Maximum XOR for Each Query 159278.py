# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for i in nums:xor^=i
        ans = []
        k = 2**maximumBit
        for t in range(len(nums)):
            bi =[ int(i) for i in  bin(xor)[2:].zfill(maximumBit)]
            temp = 0
            n = len(bi)
            for j in range(n):
                temp += (2**(n-j-1)*(1-bi[j]))
                if temp >=k:
                    temp -= (2**(n-j-1)*(1-bi[j]))
            ans.append(temp)
            xor ^= nums[len(nums)-t-1]
        return ans 

