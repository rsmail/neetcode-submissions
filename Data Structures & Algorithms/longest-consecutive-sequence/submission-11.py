class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 in numSet:
                continue
            long = 0
            while nums[i] + long in numSet:
                long += 1
            longest = max(long, longest)
        return longest
