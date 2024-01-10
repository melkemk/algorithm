class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        nam,ty=0,0
        while(nam <len(name) and ty<len(typed)):
            c=1
            while(nam+c <len(name) and name[nam]==name[nam+c]):
                c+=1
            nam+=c
            a=0
            print(nam,end=",")
            while(ty+a <len(typed) and typed[ty+a]==name[nam-1]):
                c-=1
                a+=1
            ty+=a
            print(ty)
            # if len(nam)-nam<len(typed):return 
            if (c>0):return False
        return name[len(name)-1]==typed[len(typed)-1] and ty==len(typed) and nam==len(name)

