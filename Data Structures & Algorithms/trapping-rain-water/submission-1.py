class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = [[0] for i in range(len(height))]
        right = [[0] for i in range(len(height))]
        maxl = 0
        for i in range(len(height)):
            if i == 0:
                left[i] = 0
                maxl = max(height[i], maxl)                
            else:
                left[i] = maxl
                maxl = max(maxl, height[i])
        maxr = 0
        for i in range(len(height) - 1, -1, -1):
            if i == 0:
                right[i] = 0
                maxr = max(height[i], maxr)                
            else:
                right[i] = maxr
                maxr = max(maxr, height[i])
        
        for i in range(len(height)):
            number = min(left[i], right[i]) - height[i]
            if number > 0:
                res += number
        return res