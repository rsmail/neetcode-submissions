class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "-":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs - rhs)
            elif i == "/":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(int(lhs / rhs))
            else:
                stack.append(int(i))
        return stack[-1]
            


        