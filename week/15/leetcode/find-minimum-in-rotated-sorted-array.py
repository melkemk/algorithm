class Solution:
    def findMin(self, nums: List[int]) -> int:
        l ,r =0,len(nums)-1
        _min = inf
        while l<=r:
            mid = floor((l +r)/2)
            _min = min(_min,nums[mid],nums[l],nums[r]) 
            if nums[l] < nums[mid]:
                l = mid +1
                _min = min(_min,nums[r])
            elif nums[l] > nums[mid]:
                _min = min(_min,nums[l])
                r = mid
            else:return _min 
        return _min