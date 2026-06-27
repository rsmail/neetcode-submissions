class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pairs, [temp, idx]
        for i in range(len(temperatures)):
            if not stack:
                stack.append([temperatures[i], i])
            while stack and temperatures[i] > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1] 
                stack.pop()
            stack.append([temperatures[i], i])
        
        for i in range(len(stack)):
            res[stack[i][1]] = 0
        return res

            