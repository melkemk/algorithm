class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans=[]
        index_of_pivot=nums.index(pivot)
        for i in nums:
            if(i<pivot):
                ans.append(i)
        ans.append(pivot)
        if(len(nums)>index_of_pivot+1):
            for k in range(index_of_pivot+1,len(nums)):
                if(nums[k]==pivot):
                    ans.append(pivot)
        for i in nums:
            if(i>pivot):
                ans.append(i)
        return ans
            