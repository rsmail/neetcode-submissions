class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[l] == nums[r]:
                return nums[l]
            #if whole list is sorted (rotated n times)
            if nums[l] <= nums[m] <= nums[r]:
                return nums[l]
            #if lhs is sorted
            elif nums[l] < nums[m]:
                l = m 
            #if rhs is sorted
            else:
                if r - l == 1:
                    return min(nums[l], nums[r])                
                r = m 
        return nums[0]

            
   

        