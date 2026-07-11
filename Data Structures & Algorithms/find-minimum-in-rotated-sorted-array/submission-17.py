class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minVal = sys.maxsize
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m]: #lhs sorted or all sorted
                minVal = min(minVal, nums[l])
                l = m + 1
            else: # rhs sorted
                r = m - 1
                minVal = min(minVal, nums[m])
        return minVal
        