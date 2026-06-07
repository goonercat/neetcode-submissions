class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        n = len(heights)
        l = 0
        r = n-1
        while l<r:
            mx = max(mx,(r-l)*min(heights[l],heights[r]))
            if heights[l]>=heights[r]:
                r-=1
            else:
                l+=1
        
        return mx