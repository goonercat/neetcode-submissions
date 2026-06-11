class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        n = len(prices)
        for i in range(n-1):
            for j in range(i,n):
                mx = max(mx,prices[j]-prices[i])
        return mx