class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        longest, l = 0, 0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            while k < ((r - l + 1) - max(seen.values())):
                seen[s[l]] -= 1
                l += 1
            longest = max(longest, (r - l + 1))
            
        return longest
        