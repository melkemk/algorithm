class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left=0
        temp=k
        _max=0
        for right in range(len(answerKey)):
            if answerKey[right]=='F':
                temp-=1
            while( len(answerKey)>left and  temp==-1):
                if answerKey[left]=='F':
                    temp+=1
                left+=1
            _max=max(_max,right-left+1)
        _max=max(_max,len(answerKey)-left)
        temp=k
        left=0
        for right in range(len(answerKey)):
            if answerKey[right]=='T':
                temp-=1
            while(temp<0 and left<right):
                if answerKey[left]=='T':
                    temp+=1   
                left+=1 
            _max=max(_max,right-left+1)
        _max=max(_max,len(answerKey)-left)

        return _max
        
        