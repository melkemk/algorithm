class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # num=0
        # for i in digits:
        #     num=num*10+i
        # return list( map(int,str(num+1)))
        l=len(digits)-1
        carry=0
        if digits[l]==9:
            carry=1
            digits[l]=0
        else:digits[l]+=1
        for i in range(l-1,-1,-1):
            if digits[i]+carry>9:
                digits[i]=(digits[i]+carry)%10
                carry=1
            else:
                digits[i]=(digits[i]+carry)
                carry=0
        if carry:digits.insert(0,1)
        return digits

