class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = [] ##pairs [i, t]
        for i, t in enumerate(temperatures):
            while s and s[-1][1] < t:
                res[s[-1][0]] = i - s[-1][0]
                s.pop()
            s.append([i, t])       
        return res
        