class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeros=nums.count(0)
        ones=nums.count(1)
        zero=[0,zeros]
        one=[0,ones]
        max0=max(zeros,ones)
        ar=set()
        if zeros==ones:
            ar.update([len(nums),0])
        else:
            if zeros>ones:ar.add(len(nums))
            else:ar.add(0)
        for j,i in enumerate(nums):
            if i == 0:
                zero[0]+=1
            else:
                one[1]-=1
            if max0==zero[0]+one[1]:
                ar.add(j+1)
            else:
                if zero[0]+one[1] >max0:
                    ar.clear()
                    ar.add(j+1)
                    max0=zero[0]+one[1]
        return ar

