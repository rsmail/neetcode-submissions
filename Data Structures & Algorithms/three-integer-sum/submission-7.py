class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0:
                if val == nums[i - 1]:
                    continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if val + nums[l] + nums[r] < 0:
                    l += 1
                elif val + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res