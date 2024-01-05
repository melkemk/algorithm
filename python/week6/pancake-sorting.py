class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length=len(arr)
        ans=[]
        for i in range(len(arr)-1,0,-1):
            j=arr[:i+1].index(max(arr[:i+1]))
            x=arr[:j+1][::-1]
            for t in range(j+1):
                arr[t]=x[t]
            x=arr[:i+1][::-1]
            for t in range(i+1):
                arr[t]=x[t]
            ans.extend([j+1,i+1])
        print(arr)
        return ans
            



