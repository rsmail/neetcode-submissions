class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        maxseen = 0
        for r in range(len(s)):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                seen.remove(s[r])
                l += 1
            seen.add(s[r])
            maxseen = max(maxseen, r - l + 1)
        return maxseen
                


        