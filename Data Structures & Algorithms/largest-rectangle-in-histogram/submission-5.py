class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                start, height = stack.pop()
                maxArea = max(maxArea, (i - start) * height)
            stack.append([start, h])
        for i in stack:
            newArea = (len(heights) - i[0]) * i[1]
            maxArea = max(maxArea, newArea)
        return maxArea
