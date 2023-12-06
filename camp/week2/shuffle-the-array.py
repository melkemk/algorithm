class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        total_times=len(nums)//n
        ans=[]
        for i in range(n):
            sum=i
            for j in range(total_times):
                ans.append(nums[sum])
                sum+=n
        return ans
