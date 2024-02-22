class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = 0
        ans = [-1] *len(nums1)
        index = {i:j for j ,i in enumerate(nums2)}
        for i,j in enumerate(nums1):
            x = index[j]
            a = -1
            while x<len(nums2):
                if nums2[x]>j:
                    # print(nums2[x],j)
                    a = nums2[x]
                    break
                x +=1 
            ans[i] = a
        return ans 