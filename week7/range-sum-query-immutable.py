class NumArray:

    def __init__(self, nums: List[int]):
        self.pre=[0]
        max=0
        for i in nums:
            max+=i
            self.pre.append(max)
    def sumRange(self,left,right):
        return self.pre[right+1]-self.pre[left]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)