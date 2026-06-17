class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxf = 0
        seen = set()
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxf = max(maxf, r - l + 1)
        return maxf
