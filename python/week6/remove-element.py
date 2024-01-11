class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=0 
        while(j<len(nums)):
            while( j<len(nums)-1 and nums[j]==val):
                j+=1
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1
        if val in nums:
            return  nums.index(val) 
        else:len(nums)

        