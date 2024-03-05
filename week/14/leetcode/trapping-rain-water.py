class Solution:
    def trap(self, height: List[int]) -> int:
        
        pre = [height[0]]*len(height)
        for i in range(1,len(height)):
            pre[i] = max(pre[i-1],height[i-1])
        
        next = [height[-1]]*len(height)
        for i in range(len(height)-2,-1,-1):
            next[i] = max(next[i+1],height[i+1])
        ans = 0 
        print(pre,next)
        for i in range(1,len(height)-1):
            ans += max(min(next[i],pre[i])-height[i],0)
        return ans 