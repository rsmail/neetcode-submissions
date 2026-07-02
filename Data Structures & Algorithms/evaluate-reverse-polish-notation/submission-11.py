class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "-":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs - rhs)
            elif c == "/":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(int(lhs / rhs))
            else:
                stack.append(int(c))
        return stack[0]

            