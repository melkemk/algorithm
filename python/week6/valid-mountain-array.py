class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        large=arr.index(max(arr))
        if arr.count(max(arr))>1 or large==0 or large==len(arr)-1 :return False
        if sorted(arr[0:large])==arr[0:large] and sorted(arr[large+1::],reverse=True)==arr[large+1::]:
            if len(set(arr[0:large])) != len(arr[0:large]):return False
            if len( set( arr[large+1::] )) != len( arr[large+1::] ):return False
            return True
        return False