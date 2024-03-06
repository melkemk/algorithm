class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low ,high = 0,len(nums)-1
        mid = -1
        ans = [-1,-1]
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] < target:
                low = mid+1
            elif  nums[mid] ==target:
                ans[0] = mid
                high = mid-1
            else:
                high = mid -1
        low ,high = 0,len(nums)-1
        mid = -1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] > target:
                high = mid-1
            elif nums[mid] ==target:
                ans[1] = mid
                low = mid+1
            else:
                low = mid+1
        return ans