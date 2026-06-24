class Solution:
    def trap(self, height: List[int]) -> int:
        # so first we need to get the max l at each point into an array
        maxl = 0
        maxleft = [0] * len(height)
        for i in range(len(height)):
            maxl = max(maxl, height[i])
            maxleft[i] = maxl
        maxr = 0
        maxright = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            maxr = max(maxr, height[i])
            maxright[i] = maxr
        
        res = 0
        for i in range(len(height)):
            water = min(maxright[i], maxleft[i]) - height[i]
            if water > 0:
                res += water
        return res
        
        

        