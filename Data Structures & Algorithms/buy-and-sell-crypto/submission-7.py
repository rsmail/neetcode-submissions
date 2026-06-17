class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        prof = 0
        while r < len(prices):
            dif = prices[r] - prices[l]            
            prof = max(prof, dif)
            if dif < 0:
                l = r
            r += 1
        return prof