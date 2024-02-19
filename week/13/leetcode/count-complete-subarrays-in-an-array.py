class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        left ,k = 0 ,len(set(nums))
        counter = Counter()
        ans = 0
        for right in range(len(nums)):
            counter[nums[right]] += 1
            # print(counter)
            while len(counter) == k:
                counter[nums[left]]-=1
                if counter[nums[left]] == 0:del counter[nums[left]]
                left += 1
                ans += len(nums) - right
                # print(ans,right)
                
        return ans
