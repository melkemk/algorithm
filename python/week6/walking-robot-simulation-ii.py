class Robot:
    def __init__(self, width: int, height: int):
        self.ind=[0,0]
        self.width=width
        self.height=height
        self.position=["East","North","West","South"]
        self.pos=0
        self.s=0
        self.perimeter=2*self.width+height-2+height-2
    def step(self, num: int) -> None:
        self.s+=num
        t=self.s%(self.perimeter)
        # print(
        # print(t,s)
        # print(s,t,"aaa")
        if t+1>2*self.width+self.height-2 or t==0 :
            print(1)
            self.ind=[0, self.perimeter-t]
            if t==0:self.ind=[0, 0]
            self.pos=3
        elif  self.width+self.height-2<t:
            # print(2*self.width+self.height-2,t)
            self.ind=[2*self.width+self.height-2-t-1,self.height-1]
            self.pos=2
            # print(self.ind)
        elif  self.width-1<t:
            # print(3)
            self.ind=[self.width-1, t-self.width+1]
            self.pos=1
            # print(self.ind)
        else:
            # print(4)
            self.ind=[t,0]
            self.pos=0
            # print(self.ind,self.s)
    def getPos(self) -> List[int]:
        return self.ind 
    def getDir(self) -> str:
        return self.position[self.pos]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()