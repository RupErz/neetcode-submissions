class Solution:
    def checkValidString(self, s: str) -> bool:
        stackLeftParen = []
        stackStar = []

        for i in range(len(s)):
            if s[i] == "(":
                stackLeftParen.append(i)
            elif s[i] == "*":
                stackStar.append(i)
            else:
                if stackLeftParen:
                    stackLeftParen.pop()
                elif stackStar:
                    stackStar.pop()
                else:
                    return False
        
        # If left paren stack is non-empty = left > close
        # Constantly pop star and left until left is null
        # Condition: star idx > left idx => valid
        if stackLeftParen:
            if not stackStar:
                return False

            curLeft = stackLeftParen.pop()
            curStar = stackStar.pop()

            while stackLeftParen and stackStar: 
                if curLeft < curStar:
                    curLeft = stackLeftParen.pop()
                    curStar = stackStar.pop()
                else:
                    curStar = stackStar.pop()
            
            return False if stackLeftParen else True

        return True        
        
        
                

        # openP = 0
        # closeP = 0
        # star = 0
        # # Track # open paren, # closing paren
        # # Rules: close <= open
        # for i in s:
        #     if i == "(":
        #         openP += 1
        #     elif i == ")":
        #         closeP += 1
        #         # Guard against condition 
        #         if closeP > openP + star:
        #             return False
        #     else:
        #         star += 1
        
        # gap = abs(openP - closeP)
        # return True if star >= gap else False