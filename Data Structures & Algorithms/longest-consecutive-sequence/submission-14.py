class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for i in nums:
            if (i - 1) in seen:
                continue
            long = 0
            while i + long in seen:
                long += 1
            longest = max(long, longest)
        return longest

        