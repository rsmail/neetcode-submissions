class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        l = 0
        resLen = int(sys.maxsize)
        res = ""
        for r in range(len(s)):
  
            
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                curLen = (r - l + 1)
                cur = s[l : r + 1]
                if curLen < resLen:
                    resLen = curLen
                    res = cur
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] + 1 == countT[s[l]]:
                    have -= 1
                l += 1
                
        return res


        