class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums2:
            if i in nums1:
                ans.append(nums1.pop(nums1.index(i)))
        return ans