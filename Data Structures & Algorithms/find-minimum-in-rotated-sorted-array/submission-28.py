class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = sys.maxsize
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m]: #lhs sorted
                res = min(res, nums[l])
                l = m + 1
            else: #rhs sorted
                res = min(res, nums[m])
                r = m 
        return res
        