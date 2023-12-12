class OrderedStream:

    def __init__(self, n: int):
        self.pointer=0
        self.n=n
        self.l=[0 for i in range(n)]
        self.now=0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.l[idKey-1]=value
        x=[]
        while( self.pointer <self.n and self.l[self.pointer]):
            x+=[self.l[self.pointer]]
            self.pointer+=1
        return x
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)