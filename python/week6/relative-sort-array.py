class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        di=sorted(list(set(arr1)-set(arr2)))
        ar=[]
        for i in arr2:
            ar+=[i for j in range(arr1.count(i))]
        for i in di:
            ar+=[i for j in range(arr1.count(i))]
        return ar