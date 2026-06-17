class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = 1 + seen.get(nums[i], 0)
        largest_keys = sorted(seen, key=seen.get, reverse=True)
        
        return largest_keys[:k]

        