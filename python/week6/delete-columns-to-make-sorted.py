class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ar=[list(i) for i in strs]
        a=list(zip(*ar))
        j=0
        print(a)
        for i in a:
            x="".join(i)
            # print(x
            if x !="".join(sorted(x)):j+=1
        return j