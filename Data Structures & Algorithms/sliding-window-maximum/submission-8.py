class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = r= 0
        q = collections.deque() # using indeices here

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # if the left val is out of bounds in q
            if l > q[0]:
                q.popleft()
            
            #check that r is the size of k so that we can start iterating
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output