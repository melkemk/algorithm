class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        su=0
        for i in range(k):
            su+=nums[i]
        ma=su
        for i in range(k,len(nums)):
            print(i,k-i)
            su-=nums[i-k]
            su+=nums[i]
            ma=max(su,ma)
        return ma/k