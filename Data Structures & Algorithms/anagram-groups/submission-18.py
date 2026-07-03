class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for i in range(len(strs)):
            count = [0] * 26
            for c in strs[i]:
                count[(ord(c) - ord("a"))] += 1
            freq[tuple(count)].append(strs[i])
        return list(freq.values())
        
        