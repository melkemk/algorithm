# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans  = []
        a = [int(i) for i in a]
        b = [int(i) for i in b]
        i = len(a)-1
        j = len(b)-1
        carry = 0 
        while i>-1 and j >-1:
            temp = carry + a[i] + b[j]
            print(temp,temp%2,carry)
            ans.append(temp%2)
            if temp >1:
                carry  = 1
            else:carry = 0 
            i -=1 
            j -= 1  
        while i>-1:
            temp = carry + a[i] 
            ans.append(temp%2)
            if temp >1:
                carry  = 1
            else:carry = 0 
            i -= 1 
        while j>-1:
            temp = carry + b[j] 
            ans.append(temp%2)
            if temp >1:
                carry  = 1
            else:carry = 0 
            j -= 1 
        if carry:
            ans.append(carry)
        return "".join(str(i) for i in ans [::-1])