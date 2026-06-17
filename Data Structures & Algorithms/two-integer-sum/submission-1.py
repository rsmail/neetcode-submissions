class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            x = target - val
            if x in seen:
                return[seen[x], i]
            seen[val] = i