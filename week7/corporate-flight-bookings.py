class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ar=[0]*(n+1)
        for booking in bookings:
            ar[booking[0]-1]+=booking[2]
            
            ar[booking[1]]-=booking[2]
        _sum=0
        for i in range(n):
            _sum=ar[i]+_sum
            ar[i]=_sum
        return ar[:-1]

            