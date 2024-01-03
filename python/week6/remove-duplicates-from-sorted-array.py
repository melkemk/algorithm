class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left,right=0,1
        for i in range(len(nums)-1):
            if nums[i+1]!=nums[i]:
                nums[left]=nums[i]
                left+=1
        if nums[left-1]!=nums[len(nums)-1]:nums[left]=nums[len(nums)-1]
        return left+1