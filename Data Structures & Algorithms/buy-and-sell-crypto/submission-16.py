class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        most = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                most = max(most, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return most