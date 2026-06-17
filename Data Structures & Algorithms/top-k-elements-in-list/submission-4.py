class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums) + 1)]
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        for key, val in freq.items():
            count[val].append(key) 
        res = []
        for i in range(len(count) - 1, -1, -1):
            if count[i] == []:
                continue
            for j in count[i]:
                res.append(j)
                if len(res) == k:
                    return res

        