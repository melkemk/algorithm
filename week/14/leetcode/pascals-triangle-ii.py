class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex ==0  :
            return [1]
        x = self.getRow(rowIndex-1)
        ar = [1]*(rowIndex+1)
        for i in range(len(x)-1):
            ar[i+1] = x[i]+x[i+1]
        return ar
