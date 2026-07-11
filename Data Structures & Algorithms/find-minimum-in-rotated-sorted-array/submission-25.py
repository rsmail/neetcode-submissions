class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = sys.maxsize
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            res = min(res, nums[m])
            if nums[l] <= nums[m]: #lhs sorted
                l = m + 1
            else: #rhs sorted
                r = m - 1
        return res
        