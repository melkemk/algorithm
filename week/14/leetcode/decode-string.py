class Solution:
    def decodeString(self, s: str) -> str:
        def decode(inx,s):
            # print(inx,temp)
            temp = ""
            num  = 0 
            while inx<len(s):
                if s[inx].isdigit():
                    num = num*10 + int(s[inx])
                elif s[inx] == ']':
                    return temp,inx
                elif s[inx] =='[':
                    t,inx =  (decode(inx+1,s))
                    temp += num*t 
                    num  = 0 
                else:
                    temp += s[inx]
                inx += 1
            return temp
        # print(decode(0,s))
        return decode(0,s)