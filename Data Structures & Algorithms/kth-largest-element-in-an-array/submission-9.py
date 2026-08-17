class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        while k > 0:
            num = nums.pop()
            k -= 1
            if k == 0:
                return num
