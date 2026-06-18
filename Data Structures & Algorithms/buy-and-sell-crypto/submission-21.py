class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProf = 0
        while r < len(prices):
            prof = prices[r] - prices[l]
            maxProf = max(maxProf, prof)
            if prices[l] > prices[r]:
                l = r
            r += 1
                
        return maxProf

        
        