class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left,right,temp=0,0,0
        total=0
        nums=[i%2 for i in nums]
        while(right<len(nums)):
            while( right<len(nums) and k>temp):
                if nums[right]:temp+=1
                right+=1
            if temp==k:
                l,r=1,1
                while(left <len(nums) and not nums[left]):
                    l+=1
                    left+=1
                left+=1
                temp-=1
                while(right<len(nums) and not nums[right]):
                    r+=1
                    right+=1
                total+=(l*r)
        return total
