class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        res, resLen = [-1, -1], sys.maxsize
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if resLen > (r - l + 1):
                    resLen = (r - l + 1)
                    res = [l, r]
                
                if s[l] in countT and window[s[l]] - 1 < countT[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        l, r = res
        if resLen != sys.maxsize:
            return s[l:r+1]
        else:
            return ""
