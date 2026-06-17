class Solution:
    def trap(self, height: List[int]) -> int:
        #find max l
        maxl = [[] for i in range(len(height))]
        l = 0
        maxr = [[] for i in range(len(height))]
        r = 0
        for i in range(len(height)):
            maxl[i] = l
            l = max(l, height[i])
            
        for i in range(len(height) - 1, -1, -1):
            maxr[i] = r
            r = max(r, height[i])
        
        res = 0
        for i in range(len(height)):
            wat = min(maxr[i], maxl[i]) - height[i]
            if wat > 0:
                res += wat


        return res        
            
