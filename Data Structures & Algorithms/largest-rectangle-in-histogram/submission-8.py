class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #[idx, height]
        maxArea = 0
        for i, h in enumerate(heights):
            start = i 
            while stack and h < stack[-1][1]:
                start = stack[-1][0]
                height = stack[-1][1]
                stack.pop()

                maxArea = max(maxArea, (i - start) * height)

            stack.append([start, h])
  
        for i in range(len(stack)):
            newArea = (len(heights) - stack[i][0]) * stack[i][1]
            maxArea = max(maxArea, newArea)
        return maxArea
        