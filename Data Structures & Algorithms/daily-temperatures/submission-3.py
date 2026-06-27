class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force method

        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            j = i + 1
            if i == len(temperatures) - 1:
                res[i] = 0
                continue        
            count = 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                if j == len(temperatures) - 1 and temperatures[j] <= temperatures[i]:
                    count = 0 
                else:
                    count += 1
                j += 1

            res[i] = count
        return res
            