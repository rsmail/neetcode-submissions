class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0
        q = collections.deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #check if we need to pop l
            if l > q[0]:
                q.popleft()
            
            #check if we are at size k
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res