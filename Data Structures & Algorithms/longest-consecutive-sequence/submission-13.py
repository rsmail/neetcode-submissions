class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxCount = 0
        for i in range(len(nums)):
            if (nums[i] - 1) in seen:
                continue
            else:
                count = 0
                while (nums[i] + count) in seen:
                    count += 1
            maxCount = max(count, maxCount)
        return maxCount
        