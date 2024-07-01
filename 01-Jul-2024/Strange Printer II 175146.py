# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        _set = set()
        N,M = len(targetGrid),len(targetGrid[0])

        for i in targetGrid:
            for j in i:
                _set.add(j)
        graph = defaultdict(list)
        ingoing = defaultdict(int)
        for i in _set:
            all = set()
            i_min,i_max,j_min,j_max = inf,0,inf,0
            for ii in range(N):
                for j in range(M):
                    if targetGrid[ii][j]==i:
                        i_min = min(ii,i_min)
                        i_max = max(i_max,ii)
                        j_max = max(j_max,j)
                        j_min = min(j_min,j)
            for ii in range(i_min,i_max+1):
                for j in range(j_min,j_max+1):
                    if targetGrid[ii][j]!=i and  targetGrid[ii][j] not  in all :
                        graph[targetGrid[ii][j]].append(i)
                        all.add(targetGrid[ii][j])
                        ingoing[i] += 1

        queue = deque() 
        ans = 0
        for i in _set:
            if ingoing[i]==0:
                queue.append(i)
        print(graph,ingoing,queue)

        while queue:
            last = queue.popleft()
            ans += 1 
            for i in graph[last]:
                ingoing[i] -=1
                if ingoing[i] ==0:
                    queue.append(i)
        return len(_set) ==ans

