class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ar = [0] * len(s)
        su = 0
        t=['a']*len(s)
        for shift in shifts:
            if shift[2]==1:
                ar[shift[0]] += 1
                if shift[1] + 1 !=len(ar): 
                    ar[shift[1] + 1] -= 1
            else:
                ar[shift[0]] -= 1 
                if shift[1] + 1 !=len(ar): 
                     ar[shift[1] + 1] += 1
        print(ar)
        su=0
        for i in range(len(ar)):
            su+=ar[i]
            ar[i] = su
        print(ar)
        for i in range(len(ar)):
            o = ord(s[i]) - ord("a")
            o += ar[i]
            o %= 26
            t[i] = chr(ord("a" )+ o)
        return "".join(i for i in t)
