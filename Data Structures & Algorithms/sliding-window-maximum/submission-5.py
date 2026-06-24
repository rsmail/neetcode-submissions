class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        q = collections.deque()
        res = []

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            # now we need to remove the leftmost index from the deque if 
            # its larger than the current l
            if l > q[0]:
                q.popleft()
            
            # now we need to update the result if r + 1 is > = k
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res