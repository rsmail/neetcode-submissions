class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        maxWindow = 0
        l = 0
        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l += 1

            count.add(s[r])
            maxWindow = max(maxWindow, (r - l + 1))
        return maxWindow
        