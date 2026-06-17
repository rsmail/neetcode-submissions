class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        strS, strT, = {}, {}

        for i in range(len(s)):
            strS[s[i]] = strS.get(s[i], 0) + 1
            strT[t[i]] = strT.get(t[i], 0) + 1
        return strS == strT

        
        