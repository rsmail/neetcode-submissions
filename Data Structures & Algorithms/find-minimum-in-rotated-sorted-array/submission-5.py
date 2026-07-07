class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]: #lhs sorted
                l = m + 1
            else: #rhs sorted 
                r = m


        return nums[l]

            
   

        