class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=[]
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            t=nums[i]+nums[l]+nums[r]
            while(  r>l):
                ans.append([nums[i],nums[l],nums[r]])
                if t>target and r>l:
                    r-=1
                elif t<target and r>l:
                    l+=1
                else:return target
                t=nums[i]+nums[l]+nums[r]
            if l!=r:ans.append([nums[i],nums[l],nums[r]])

        # print(  (sorted(ans,key=lambda x:abs(sum(x)-target)))
        for i in ans:
            if sum(i)==target:print(111)
        return sum(sorted(ans,key=lambda x:abs(sum(x)-target))[0])
