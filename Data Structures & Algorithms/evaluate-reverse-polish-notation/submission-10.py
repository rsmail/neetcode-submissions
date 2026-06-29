class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in range(len(tokens)):
            if tokens[i] == "+":            
                s.append(s.pop() + s.pop())
            elif tokens[i] == "*":
                s.append(s.pop() * s.pop())
            elif tokens[i] == "-":
                rhs = s.pop()
                lhs = s.pop()
                s.append(lhs - rhs)
            elif tokens[i] == "/":
                rhs = s.pop()
                lhs = s.pop()
                s.append(int(lhs / rhs))

            else:
                s.append(int(tokens[i]))
        return s[0]