class Solution:
    def trap(self, height: List[int]) -> int:
        #first we need to find the highest lefts
        lMax = 0
        left = [0] * len(height)
        for i in range(len(height)):
            if i > 0:
                lMax = max(lMax, height[i - 1])
            left[i] = lMax

        RMax = 0
        right = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            if i < len(height) - 1:
                RMax = max(RMax, height[i + 1])
            right[i] = RMax
        res = 0
        for i in range(len(height)):
            water = min(left[i], right[i]) - height[i]
            if water > 0:
                res += water
        
        return res