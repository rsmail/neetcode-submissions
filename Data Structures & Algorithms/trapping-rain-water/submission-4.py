class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [[0] for i in height]
        lMax = 0
        for i in range(len(height)):
            leftMax[i] = lMax
            lMax = max(lMax, height[i])
        
        rightMax =[[0] for i in height]
        rMax = 0
        for i in range(len(height) - 1, -1, -1):
            rightMax[i] = rMax
            rMax = max(rMax, height[i])
        
        res = 0

        for i in range(len(height)):
            water = min(leftMax[i], rightMax[i]) - height[i]
            if water > 0:
                res += water
        return res
            
        