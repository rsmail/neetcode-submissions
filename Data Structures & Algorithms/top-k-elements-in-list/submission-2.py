class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            seen[nums[i]] = 1 + seen.get(nums[i], 0)

        for key, item in seen.items():
            freq[item].append(key)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        