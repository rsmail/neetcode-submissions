class Solution:
    def isValid(self, s: str) -> bool:
        map = {"]" : "[", "}" : "{", ")" : "("}
        stack = []
        for i in s:
            if i not in map:
                stack.append(i)
            else:
                if not stack or map[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        else:
            return True

        