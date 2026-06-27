class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for c in s:
            if stack and c in closeToOpen:
                if stack[-1] != closeToOpen[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return True if not stack else False

