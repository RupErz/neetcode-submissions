class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        # Subsequence: DFS, pick or not pick to ensure no duplication
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            result = 0
            if s[i] == t[j]:
                # You can pick this up 
                result += dfs(i + 1, j + 1)

            # Otherwise you can skip
            result += dfs(i + 1, j)
            memo[(i, j)] = result

            return result
        
        return dfs(0, 0)

