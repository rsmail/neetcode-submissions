class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        highest = 0
        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            highest = max(highest, (height * width))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return highest
        

        