class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        i = len(nums)-2
        ans = 0 
        replace =0 
        while i >-1:
            if nums[i]>nums[i+1]:
                    x=0
                    x += (ceil(nums[i]/nums[i+1]))
                    replace += (x-1)
                    nums[i]= nums[i]//x 
            i -= 1
        return replace
        