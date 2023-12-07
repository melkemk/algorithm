class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        right,left,ans=[0]*len(boxes),[0],[]
        x1=0
        x2=0
        for i in range(1,len(boxes)):
            if(boxes[i-1]=='1'):
                x1+=1
            x2+=x1
            left.append(x2)
        x1,x2=0,0
        for i in range(len(boxes)-2,-1,-1):
            if(boxes[i+1]=='1'):
                x1+=1
            x2+=x1
            right[i]=(x2)
        for i in range(len(boxes)):
            ans.append(right[i]+left[i])
        return ans