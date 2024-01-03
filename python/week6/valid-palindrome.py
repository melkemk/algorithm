class Solution:
    def isPalindrome(self, s: str) -> bool:
        print('1'.lower())
        ar=[]
        for i in s:
            if i.isalnum():ar.append(i.lower() )
        print(ar)
        for i in range( floor(len(ar)//2)):
            if ar[i]!=ar[len(ar)-i-1]:
                return False
        return True
        