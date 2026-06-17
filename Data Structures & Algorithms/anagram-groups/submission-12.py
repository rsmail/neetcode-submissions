class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for i in range(len(strs)):
            count = [0] * 26
            for s in strs[i]:
                count[ord(s) - ord('a')] += 1
            freq[tuple(count)].append(strs[i])

        res = []
        for key, item in freq.items():
            res.append(item)
        return res