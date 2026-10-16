class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            if (i, j) in memo:
                return memo[(i, j)]
            
            if i < len(s) and (s[i] == p[j] or p[j] == "."):
                if j + 1 < len(p):
                    if p[j + 1] == "*":
                        memo[(i, j)] = (
                            dfs(i, j + 2)
                            or 
                            dfs(i + 1, j)
                        )
                    else:
                        memo[(i, j)] = dfs(i + 1, j + 1)
                else:
                    memo[(i, j)] = dfs(i + 1, j + 1)
                
            else:
                if j + 1 < len(p):
                    if p[j + 1] == "*":
                        memo[(i, j)] = dfs(i, j + 2)
                    else:
                        memo[(i, j)] = False
                else:
                    memo[(i, j)] = False
            
            return memo[(i, j)]

        return dfs(0, 0)


