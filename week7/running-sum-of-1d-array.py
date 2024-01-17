class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        self.pre=[]
        max=0
        for i in nums:
            max+=i
            self.pre.append(max)
        return self.pre
