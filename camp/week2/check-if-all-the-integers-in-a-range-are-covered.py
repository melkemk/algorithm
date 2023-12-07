class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        numbers=set()
        for num in ranges:
            temp={i for i in range(num[0],num[1]+1)}
            numbers.update(temp)
        # print(numbers)
        for i in range(left,right+1):
            if(i not  in numbers):
                return False
        return True