class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=[]
        smallest=None
        num=None
        ar1=None
        ar1=None
        if(len(list1)>len(list2)):
            ar1=list1.copy()
            ar2=list2.copy()
        else:
            ar1=list2.copy()
            ar2=list1.copy()
        for i,j in enumerate(ar1):
            if j in ar2:
                num=i+ar2.index(j)
                if smallest or smallest==0:
                    smallest=min(num,smallest)
                else:
                    smallest=num
                ans.append([j,num])
        print(smallest,ans)
        return [i for i,j in ans if j==smallest ]