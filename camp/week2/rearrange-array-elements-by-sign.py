class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives=[j for j in (nums) if j>0]
        negatives=[j for j in (nums) if j<0 ]
        ans=[]
        for i in range(len(nums)//2):
            ans.append(positives[i])
            ans.append(negatives[i])
        return ans
