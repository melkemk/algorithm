class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max=1
        mult=1
        for i in nums:
            mult*=i
        pre=[]
        if(nums.count(0)>1):
            return [0 for i in nums]
        if(nums.count(0)==1):
            mult=1
            for i in nums :
                if i!=0:
                    mult*=i
            pre= [0 for i  in  nums]
            pre[nums.index(0)]=mult
            return pre
                
        else:
            for i in nums:
                pre.append(mult//i) 
        return  pre