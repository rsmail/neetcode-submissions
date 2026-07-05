class Solution:
    def findMin(self, nums: List[int]) -> int:
        small = sys.maxsize
        for i in nums:
            small = min(small, i)
        return small
        