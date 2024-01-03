class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        maxa=0
        for i in range(len(processorTime)):
            x=max(tasks[i*4:i*4+4])
            x+=processorTime[i]
            maxa=max(maxa,x)
        return maxa
