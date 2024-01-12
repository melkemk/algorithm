class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sums=[0]
        su=0
        _max=0
        for i in nums:
            su+=i
            sums.append(su)
        left=0
        _dic=defaultdict()
        for right in range(len(nums)):
            _dic[nums[right]]=_dic.get(nums[right],0)+1
            last=left
            while(left<len(nums) and _dic[nums[right]]==2):
                _dic[nums[left]]-=1
                _max=max(sums[right]-sums[last],_max)
                left+=1
            print(left,_max)
            _max= max (sums[right]-sums[left],_max)
        _max= max (sums[len(nums)]-sums[left],_max)
        return _max