class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def dfs(openP, closeP, current):
            if openP == closeP == n:
                result.append(current)
                return

            if openP < n:
                dfs(openP + 1, closeP, current + "(")

            if openP > closeP:
                dfs(openP, closeP + 1, current + ")")
        
        dfs(0, 0, "")
        return result 
            

