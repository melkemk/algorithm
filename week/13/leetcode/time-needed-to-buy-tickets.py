class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i =0
        time = 0 
        while tickets[k]!=0:
            if not  tickets[i]:time  -= 1
            if tickets[i]>0: tickets[i] -= 1
            i += 1
            if i ==len(tickets):i =0 
            time += 1
        return time 