class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = [[] for i in range(len(nums) + 1)]
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        for key, val in freq.items():
            count[val].append(key)
        res = []
        for i in range(len(count) - 1, -1, -1):
            for i in count[i]:
                res.append(i)
                if len(res) == k:
                    return res



        