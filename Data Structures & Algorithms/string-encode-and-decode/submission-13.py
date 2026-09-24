class Solution:

    def encode(self, strs: List[str]) -> str:
        #list of strings ["hello", "world"]
        #turn into one string
        #"5#hello5#world"
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        #string consisting of "5#hello5#world"
        #iterte through for "#" then len = [i : j]

        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = length + 1 + j
        return res

            

