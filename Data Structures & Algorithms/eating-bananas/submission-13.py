class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        mink = sys.maxsize
        l, r = 1, max(piles)
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / k)
            if hours <= h:
                mink = min(mink, k)
                r = k - 1
            else: # took too long
                l = k + 1
        return mink


            
        

        


        