class RecentCounter:

    def __init__(self):
        self.queue = []
        self.i =0 
    def ping(self, t: int) -> int:
        i = self.i 
        self.queue.append(t)
        while len(self.queue) >i and self.queue[i] < t-3000:
            i += 1
        self.i = i
        return len(self.queue) - i




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)