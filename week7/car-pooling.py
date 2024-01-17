class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pre=[0]*1001
        for i in trips:
            for j in range(i[1]-1,i[2]-1):
                pre[j]+=i[0]
            # pre[i[2]]-=i[0]
        for i in range(len(pre)):
            print(pre[i])
            if pre[i]>capacity:return False
        return True
        
