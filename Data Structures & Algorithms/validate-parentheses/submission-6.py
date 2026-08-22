class Solution:
    def isValid(self, s: str) -> bool:
        #openbracket = add to stack
        #closebracket = start checking
        #before pop a stack make sure its not empty
        #if we reach the end and stack still not empty => False (#brackets not even)
        closeToOpen = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = [] #stack.pop : remove last + show up last val
        #stack[-1] return last value ( the top of the stack)
        for i in s :
            if i in closeToOpen :
                if stack and stack[-1] == closeToOpen[i] :
                    stack.pop()
                else :
                    return False
            else :
                stack.append(i)
        return True if not stack else False 
