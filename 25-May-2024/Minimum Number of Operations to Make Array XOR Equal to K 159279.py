# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        final_xor = 0

        for i in nums:
            final_xor = final_xor ^ i

        return (final_xor^k).bit_count()