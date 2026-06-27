class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count, window = [0] * 26, [0] * 26
        # we need to iterate through s1 first to get its frequencies as well as s2
        
        for i in range(len(s1)):
            count[(ord(s1[i]) - ord('a'))] += 1
            window[(ord(s2[i]) - ord('a'))] += 1
        matches = 0
        for i in range(26):
            if window[i] == count[i]:
                matches += 1 
        l = 0
        
        for r in range(len(s1), len(s2)):
            
            if window == count:
                return True
            #what do we need to do
            # we need to now slide through s2 at a window len of s1... if count == window return true
            #r = first new index
            #we need to remove winow l, l += 1
            # we need to add r
            index = ord(s2[l]) - ord('a')
            window[index] -= 1
            if window[index] == count[index]:
                matches += 1
            elif window[index] + 1 == count[index]:
                matches -= 1
            l += 1

            index = ord(s2[r]) - ord('a')
            window[index] += 1

            if window[index] == count[index]:
                matches += 1
            elif window[index] - 1 == count[index]:
                matches -= 1
        return matches == 26


            