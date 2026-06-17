class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxprof = 0
        while r < len(prices):
            prof = prices[r] - prices[l]
            maxprof = max(maxprof, prof)
            if prof < 0:
                l = r
            r += 1
        return maxprof
            

        