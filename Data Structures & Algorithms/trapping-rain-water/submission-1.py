class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ml = [0]*n
        mr = [0]*n
        mlr = [0]*n
        ml[0] = height[0]
        for i in range(1,n):
            ml[i] = max(ml[i-1],height[i])
        mr[n-1] = 0
        for i in range(n-2,-1,-1):
            mr[i] = max(height[i+1],mr[i+1])
        for i in range(n):
            mlr[i] = min(ml[i],mr[i])
        lst = [0]*n
        for i in range(n):
            lst[i] = mlr[i]-height[i]
        for i in range(n):
            if lst[i]<0:
                lst[i] = 0
        return sum(lst)