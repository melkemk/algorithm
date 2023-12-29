class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:return 0
        if num>=0:
            nums=[ (i) for i in str(num)]
            nums.sort()
            print(nums)
            for i,j in enumerate(nums):
                if j!='0':
                    nums[0],nums[i]=nums[i],nums[0]
                    break
            print(nums)
            return int("".join(nums))
        else:
            num=-1*num
            nums=[ i for i in str(num)]
            ans=[]
            nums.sort()
            nums=nums[::-1]
            return -1* int("".join(nums))