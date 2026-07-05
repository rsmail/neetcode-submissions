class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        #now we have the frequencies of each unique element
        #now we need to put these into count
        for element, freq in freq.items():
            count[freq].append(element)
        #we now have all of the counts set up in lists.
        #iterate backwards and append to new list res
        res = []
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                    res.append(n)
                    if len(res) == k:
                        return res

  
            