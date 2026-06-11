class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l+1
        mp = 0
        while r<len(prices):
            pf = prices[r]-prices[l]
            if pf<0:
                l=r
            else:
                if pf>mp:
                    mp = pf
            r+=1
        return mp