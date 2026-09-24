class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        #iterate through nums, if nums[i] - 1 not in seen, then its a start
        for i in range(len(nums)):
            if nums[i] - 1 in seen: # not a start of a sequence
                continue
            #start of a sequence
            j = 0            
            while nums[i] + j in seen:
                j += 1
            longest = max(longest, j)
        return longest

            
        