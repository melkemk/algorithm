class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        fourth=(len(arr)//4)
        for i in range(len(arr)-fourth+1):
            if(arr[i]==arr[i+fourth]):return arr[i]