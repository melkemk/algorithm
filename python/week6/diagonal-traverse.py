class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # i,j=0,0
        # ans=[]
        # while(i!=len(mat) and j!=len(mat[0])):
        #     ans.append(mat[i][j])
        #     if i==0 :
        #         if j<len(mat[0])-1:
        #             j+=1
        #         else:
        #             i+=1
        #         while(i<len(mat) and j>=0):
        #             ans.append(mat[i][j])
        #             i+=1
        #             j-=1
        #     else:
        #         if i!=len(mat)-1:
        #             i+=1
        #         else:
        #             j+=1
        #         while(i>=0 and j<len(mat[0])):
        #             ans.append(mat[i][j])
        #             i-=1
        #             j+=1
        # # ans.append(mat[i-1][j])
        # return ans
        di=defaultdict(list)
        for i,row in enumerate(mat):
            for j,col in enumerate(row):
                di[i+j].append(col)
        li=[]
        for i,j in di.items():
            if i%2==0:
                li.extend((j[::-1]))
            else:li.extend(j)
        return li

