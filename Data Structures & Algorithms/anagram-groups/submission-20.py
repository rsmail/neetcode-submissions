class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = collections.defaultdict(list)
        for i in strs:
            freq = [0]*26
            for c in i:
                freq[ord("a") - ord(c)] += 1
            count[tuple(freq)].append(i)
    
        return list(count.values())
        
        