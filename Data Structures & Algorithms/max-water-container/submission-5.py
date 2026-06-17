class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            most = max(most, (width * height))
            if heights[l] <= heights[r] and l < r:
                l += 1
            elif heights[l] > heights[r] and l < r:
                r -= 1
        return most