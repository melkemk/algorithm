# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(2) ]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        self.root = TrieNode()
        ans = 0 
        for i,j in enumerate(nums):
            start = self.root
            num = bin(j)[2:].zfill(31)

            num = [int(n) for  n in num]
            temp = []
            for b in range(31):
                if start.children[1-num[b]]:
                    start = start.children[1-num[b]] 
                    temp.append(1)
                elif i!=0:
                    start = start.children[num[b]] 
                    temp.append(0)
            if temp:
                ans = max(ans, int("".join(str(t) for t in temp), 2))
            start = self.root

            for b in range(31):
                if start.children[num[b]]==None:
                    start.children[num[b]] = TrieNode()
                start = start.children[num[b]]
        return (ans)
