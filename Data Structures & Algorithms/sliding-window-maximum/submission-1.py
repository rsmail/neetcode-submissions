class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []
        while r < len(nums):
            maxEl = -sys.maxsize
            for i in range(l, r + 1):
                maxEl = max(maxEl, nums[i])
            res.append(maxEl)
            l += 1 
            r += 1
        
        return res


        