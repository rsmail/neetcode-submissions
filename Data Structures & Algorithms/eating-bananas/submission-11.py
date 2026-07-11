class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minRate = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / k)
            if hours > h:
                #too small
                l = k + 1
            else:
                r = k - 1
                minRate = min(minRate, k)
        return minRate