class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() #putting in indices here
        l = 0
        res = []
        for r in range(len(nums)):

            #steps
            ##check if q[-1] < nums[i]
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            
            ##if r >= k, update res and l 
            if r + 1 >= k:
                res.append(nums[q[0]])
                if q[0] == l:
                    q.popleft()
                l += 1

        return res
            


        