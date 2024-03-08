class TimeMap:

    def __init__(self):
        self.ar = defaultdict(list)
        self.nums = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ar[key].append([key,value])
        self.nums[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect_right(self.nums[key],timestamp)
        if i<=len(self.ar[key]) and i:
            return self.ar[key][i-1][1]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)