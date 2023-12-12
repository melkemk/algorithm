class UndergroundSystem:

    def __init__(self):
        self.check=defaultdict(tuple)
        self.time=defaultdict(tuple)
        self.info=[]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # if id in self.check:
        #     return None
        self.check[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # print(self.check,id,stationName)
        x=list(self.check[id])
        x[1]=t-x[1]
        # del self.check[id]
        if (x[0] ,stationName) in self.time:
            self.time[(x[0] ,stationName)]=[x[1]+self.time[(x[0] ,stationName)][0],self.time[(x[0] ,stationName)][1]+1]
        else:
            self.time[(x[0] ,stationName)]=[x[1],1]
        # print(self.time)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # print(self.time[startStation+endStation])
        return self.time[(startStation,endStation)][0]/self.time[(startStation,endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)