class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        seen = defaultdict(list)
        for i in range(len(strs)):
            freq = [0] * 26
            for s in strs[i]:
                freq[ord(s) - 97] += 1
            seen[str(freq)].append(strs[i])
      
        return (list(seen.values()))
        
