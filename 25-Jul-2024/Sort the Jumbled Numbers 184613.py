# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return [j for i,j in sorted([(int(''.join(map(lambda x: str(mapping[int(x)]), str(i)))), i) for i in nums],key=lambda x: x[0])]

