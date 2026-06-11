class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we just have to find the minumum so we pick a minimum as l and keep incerasing r so
        #that we get a max difference and keep storing the max difference in mp ,and if we
        #get a r value less than l, we keep l in place of r and then check the max profit
        l = 0
        r = l+1
        mp = 0
        while r<len(prices):
            if prices[r]<prices[l]:
                l=r
            else:
                if prices[r]-prices[l]>mp:
                    mp = prices[r]-prices[l]
            r+=1
        return mp