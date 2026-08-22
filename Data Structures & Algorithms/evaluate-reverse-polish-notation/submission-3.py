class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ['+', '-', '*', '/']
        for tokens in tokens:
            if tokens in operator :
                # starting poping from the stack, calculate and push back
                # + , * order not matter
                # -, / matter !
                if tokens == '+':
                    stack.append(stack.pop() + stack.pop())
                elif tokens == '-':
                    a,b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif tokens == '*':
                    stack.append(stack.pop() * stack.pop())
                else:
                    a,b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
            else :
                stack.append(int(tokens))
        return stack[0]