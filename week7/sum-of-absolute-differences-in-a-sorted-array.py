class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre=[0]
        ans=[]
        _sum=0
        for i in nums:
            _sum+=i
            pre.append(_sum)
        print(pre)
        for i in range(len(nums)):
            added=pre[i]
            decrement=pre[len(nums)]-added
            print(added,decrement)
            t=-1*(len(nums)-i)*nums[i]
            t+=nums[i]*i
            t+=decrement
            t-=added
            ans.append(t)
        return ans