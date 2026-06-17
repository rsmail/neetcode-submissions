class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res += str(len(strs[i]))
            res += ('%')
            res += strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            count = i
            while s[i] != '%':
                i += 1
            length = s[count : i]
            res.append(s[i + 1: int(length) + 1 + i])
            i += int(length) + 1
        return res