class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=image.copy()
        i=0
        while(i<len(image)):
            ans[i]=ans[i][::-1]
            i+=1
        i=0            
        while(i<len(image)):
            for j in range(len(image[i])):
                ans[i][j]=0 if ans[i][j] else 1
            i+=1
        return ans
