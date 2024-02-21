class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrom = list(palindrome)
        if len(palindrome) <2:return ""
        for i in range(len(palindrom)):
            if palindrome[i]!='a':
                t=palindrom[i]
                palindrom[i] = 'a'
                if all(i=='a' for i in palindrom):
                    palindrom[i]=t
                else:return "".join(palindrom)
        palindrom[-1]='b'
        return "".join(palindrom)
