class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even=sum(i for i in nums if not i%2)
        even_array=[]
        print(even)
        for j,i in queries:
            if(nums[i]%2 and j%2):
                even+=j+nums[i]
                nums[i]+=j
            elif(not j%2 and not nums[i]%2):
                even+=j
                nums[i]+=j
            elif(not nums[i]%2 and j%2):
                even-=nums[i]
                nums[i]+=j
            else: nums[i]+=j
            print(even)
            even_array.append(even)
        return even_array
        