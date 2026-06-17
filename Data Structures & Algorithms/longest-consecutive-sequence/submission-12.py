class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in numSet:
                long = 0
                while n + long in numSet:
                    long += 1
                longest = max(longest, long)
        return longest
