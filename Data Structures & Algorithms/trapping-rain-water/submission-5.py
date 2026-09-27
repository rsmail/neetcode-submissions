class Solution:
    def trap(self, height: List[int]) -> int:
        leftmost = [0] * len(height)
        leftmax = 0
        for i in range(len(height)):
            leftmost[i] = leftmax
            leftmax = max(leftmax, height[i])

        rightmost = [0] * len(height)
        rightmax = 0
        for i in range(len(height) - 1, -1, -1):
            rightmost[i] = rightmax
            rightmax = max(rightmax, height[i])

        res = 0
        for i in range(len(height)):
            water = (min(leftmost[i], rightmost[i])) - height[i]
            if water > 0:
                res += water
        return res

            
        