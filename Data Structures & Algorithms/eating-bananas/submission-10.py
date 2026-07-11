class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_rate = r

        while l <= r:
            k = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            if hours > h:
                # Too slow, increase the rate.
                l = k + 1
            else:
                # This rate works; save it and try a smaller one.
                min_rate = k
                r = k - 1

        return min_rate