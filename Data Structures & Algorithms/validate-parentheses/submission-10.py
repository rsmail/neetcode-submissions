class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}" : "{", "]" : "[", ")" : "("}
        stack = []

        for i in range(len(s)):
            if stack and s[i] in closeToOpen and closeToOpen[s[i]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack) > 0:
            return False
        else:
            return True