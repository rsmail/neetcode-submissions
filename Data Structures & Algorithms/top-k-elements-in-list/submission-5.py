class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        seen = defaultdict(list)
        for i in range(len(nums)):
            seen[nums[i]] = 1 + seen.get(nums[i], 0)
        for key, val in seen.items():
            count[val].append(key)
        res2 = []
        for i in range(len(count) - 1, -1, -1):
            for j in range(len(count[i])):
                res2.append(count[i][j])
                if len(res2) == k:
                    return res2

        
