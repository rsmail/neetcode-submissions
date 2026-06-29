class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # have this be indices 
        l, r = 0, 0
        res = []
        while r < len(nums):
            #we need a couple steps in this loop
            
            #1 update q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            #2 if left is past start of q
            if q and l > q[0]:
                q.popleft()

            #3 we are at k len, start adding to res
            if q and r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res
