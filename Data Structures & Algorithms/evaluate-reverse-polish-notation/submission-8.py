class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for c in tokens:
            if c == "+":
                s.append(s.pop() + s.pop())
            elif c == "*":
                s.append(s.pop() * s.pop())
            elif c == "-":
                rhs = s.pop()
                lhs = s.pop()
                s.append(lhs - rhs)
            elif c == "/":
                rhs = s.pop()
                lhs = s.pop()
                s.append(int(lhs / rhs))
            else:
                s.append(int(c))
        return s[0]


