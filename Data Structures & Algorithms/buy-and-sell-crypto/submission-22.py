class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0
        for r in range(len(prices)):
            prof = prices[r] - prices[l]
            maxP = max(maxP, prof)

            if prof < 0:
                l = r
        return maxP


        