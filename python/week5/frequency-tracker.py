class FrequencyTracker:
    def __init__(self):
        self.val=defaultdict(int)
        self.c=defaultdict(int)
    def add(self, number: int) -> None:
        if self.c[self.val[number]]==0 or self.c[self.val[number]]==-1:del self.c[self.val[number]]
        self.c[self.val[number]]-=1
        self.c[self.val[number]+1]+=1
        if self.c[self.val[number]]==0 or self.c[self.val[number]]==-1:del self.c[self.val[number]]
        self.val[number]+=1
    def deleteOne(self, number: int) -> None:
            # print(self.c,self.val) 
            self.c[self.val[number]]-=1
            self.c[self.val[number]-1]+=1
            if self.c[self.val[number]-1]==0 or self.c[self.val[number]-1]==-1:del self.c[self.val[number]-1]
            self.val[number]-=1
            if self.val[number]==0 or self.val[number]==-1: del self.val[number]
    def hasFrequency(self, frequency: int) -> bool:
            return self.c[frequency]!=0 and self.c[frequency]!=-1


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)