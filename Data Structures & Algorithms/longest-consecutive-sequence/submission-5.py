class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        nums.sort()
        long = 0
        i = 0
        count = 1
        while i < len(nums) - 1:
            if nums[i] + 1 == nums[i + 1]:
                count += 1
            elif nums[i] != nums[i + 1]:
                count = 1
            else:
                long = max(long, count)
            long = max(long, count)
            i += 1
        return long


        