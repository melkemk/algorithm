class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lowest=22**31 - 1
        low =22**31 - 1
        for i in range(len(nums)):
            if nums[i]<lowest:
                lowest=nums[i]
            if  nums[i] > lowest  and nums[i]<low:
                low=nums[i]
            # if lowest>low:
            #     low,lowest=lowest,low
            if nums[i]>low:return True
            # print(lowest,low)
        return False
