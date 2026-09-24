class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        freq = [[] for i in range(len(nums) + 1)] #list of lists 
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        #count now int : count
        for c, v in count.items():
            freq[v].append(c)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for item in freq[i]:
                res.append(item)
                if len(res) == k:
                    return res


        