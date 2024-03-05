class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        seanteTrue  = [ 1 for i in senate]
        rq = deque()
        dq = deque()
        
        for i,j in enumerate(senate):
            if j=='R':
                rq.append(i)
            else:
                dq.append(i)
        i  = 0 
        while dq and rq:
            i %= len(senate)
            if senate[i] == 'R' and seanteTrue[i]:
                seanteTrue[dq.popleft()] = 0 
                rq.append(rq.popleft())
            elif senate[i] == 'D' and seanteTrue[i]:
                seanteTrue[rq.popleft()] = 0 
                dq.append(dq.popleft())
            i += 1
        return "Radiant" if rq else "Dire"
        