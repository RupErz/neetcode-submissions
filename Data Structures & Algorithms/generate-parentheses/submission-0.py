class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #We need to backtrack for this => Recursion
        #Based case ? n = 3 => 3 open 3 closed
        #Cond add open ? if open < n , +1 every time add
        #Cond add close ? if close < open, +1 every time add
        stack = [] #This is global variable make sure empty it 
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n: #Base case : append to res and stop cur path
                res.append("".join(stack)) #Make into a string and append
                return
            if openN < n :
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop() #pop this value after done 
            if closedN < openN :
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res

