class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l = 0
        for r in range(len(prices)):
            if (prices[r] - prices[l]) < 0:
                l = r
            else:
                prof = max(prof, (prices[r] - prices[l]))
        return prof