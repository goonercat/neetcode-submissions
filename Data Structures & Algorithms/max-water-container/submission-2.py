class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #bruteforce
        mx = 0
        n = len(heights)
        for i in range(0,n-1):
            for j in range(i,n):
                if min(heights[i],heights[j])*abs(i-j)>mx:
                    mx = min(heights[i],heights[j])*abs(i-j)
        
        return mx