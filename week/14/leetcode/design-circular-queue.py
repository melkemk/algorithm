class MyCircularQueue:

    def __init__(self, k: int):
        self.first = 0 
        self.last = 0 
        self.k = k
        self.arr  = [-1] * k
        self.total = 0 

    def enQueue(self, value: int) -> bool:
        if self.total !=self.k :
            self.arr[self.last ] = value
            self.last += 1
            if self.last ==self.k:self.last = 0 
            self.total += 1
            return 1
    def deQueue(self) -> bool:
        if not self.isEmpty() :
            self.first += 1
            if self.first == self.k:self.first = 0 
            self.total -= 1
            return 1

    def Front(self) -> int:
        if not self.isEmpty():
            return self.arr[self.first]
        return -1
    def Rear(self) -> int:
        if not self.isEmpty():
            if self.last !=0:
                return self.arr[self.last-1]
            return self.arr[-1]
        return -1

    def isEmpty(self) -> bool:
        return self.total ==0

    def isFull(self) -> bool:
        return self.total == self.k



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()