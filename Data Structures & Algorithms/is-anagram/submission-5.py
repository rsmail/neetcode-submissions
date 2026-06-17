class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        strS, strT = {}, {}
        for i in range(len(s)):
            strS[s[i]] = 1 + strS.get(s[i], 0)
            strT[t[i]] = 1 + strT.get(t[i], 0)
        return strS == strT