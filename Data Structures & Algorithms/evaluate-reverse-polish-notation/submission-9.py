class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        stack = []
        # Valid + Constraint so either 1 or >= 3 elements

        for i in tokens:
            if len(stack) >= 2 and i in ["+", "-", "*", "/"]:
                first, second = stack.pop(), stack.pop()

                if i == "+":
                    stack.append(second + first)
                elif i == "-":
                    stack.append(second - first)
                elif i == "*":
                    stack.append(first * second)
                else:
                    stack.append(int(second / first))
            else:
                stack.append(int(i))

        return stack[0]
            
          
        
