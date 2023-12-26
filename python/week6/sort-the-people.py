class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # ans=[]
        # dic={height:i for i,height in enumerate(heights)}
        # print(dic)
        # for i in range(len(heights)-1):
        #     for j in range(i+1,len(heights)):
        #         if(heights[i]<heights[j]):
        #             heights[i],heights[j]=heights[j],heights[i]
        # print(heights)
        # for i in heights:
            # ans.append( names[dic[i]])
        a=list(zip(names,heights))
        a.sort(key=lambda i:i[1],reverse=True)
        return [i for i,j in a]