class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, maxProf = 0, 0

        for r in range(len(prices)):


            if prices[r] < prices[l]:
                l = r
            maxProf = max((prices[r] - prices[l]), maxProf)


        return maxProf
            

