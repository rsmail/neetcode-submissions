class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = len(nums)
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m]: #lhs sorted
                res = min(res, nums[l])
                l = m + 1
            else: #rhs sorted
                res = min(res, nums[m])
                r = m - 1
        return res

        