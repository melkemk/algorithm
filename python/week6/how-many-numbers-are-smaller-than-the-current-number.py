class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=[]
        sor = sorted((nums), reverse=True)
        i=0
        di={}
        while(i<len(sor)):
            j=0
            if i+1<len(sor) and  sor[i]!=sor[i+1]:
                di[sor[i]]=(len(sor)-i-1)
                print(di)
                i+=1
            elif 1+i<len(sor) and sor[i]==sor[i+1]:
                while(1+i<len(sor) and sor[i]==sor[i+1]):
                    i+=1
                di[sor[i-1]]=(len(sor)-i)
            else:
                di[sor[i]]=0
                i+=1
                # print(i)
        print(di)
        return [di[j] for j in nums]
