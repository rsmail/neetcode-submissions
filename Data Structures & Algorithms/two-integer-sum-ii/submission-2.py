class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        current = numbers[l] + numbers[r]
        while l < r and current != target:            
            if current < target:
                l += 1
                current = numbers[l] + numbers[r]
            if current > target:
                r -= 1
                current = numbers[l] + numbers[r]
        return [l + 1, r + 1]