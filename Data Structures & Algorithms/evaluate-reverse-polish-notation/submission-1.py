class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                val = stack.pop()
                if t == "+":
                    stack[-1] += val
                elif t == "-":
                    stack[-1] -= val
                elif t == "*":
                    stack[-1] *= val
                else:
                    stack[-1] = int(stack[-1] / val)
            else:
                stack.append(int(t))
        return stack[0]