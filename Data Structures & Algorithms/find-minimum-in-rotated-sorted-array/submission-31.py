class Solution:
    def findMin(self, nums: List[int]) -> int:
            l, r = 0, len(nums) - 1
            smallest = sys.maxsize
            while l <= r:
                m = (l + r) // 2
                if nums[l] <= nums[m]: #lhs sorted
                    smallest = min(nums[l], smallest)
                    l = m + 1
                else: #rhs sorted
                    smallest = min(smallest, nums[m])
                    r = m - 1
            return smallest


        