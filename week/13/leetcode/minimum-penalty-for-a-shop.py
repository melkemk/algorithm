class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = customers.count('N')
        _sum = n
        _min = [len(customers),_sum]
        for idx,i in enumerate(reversed(customers)):
            if i == "Y":
                _sum += 1
            else :
                _sum -= 1
            if _sum <= _min[1]:
                _min[0] = len(customers)-1-idx
                _min[1] =_sum
        return _min[0]
        
