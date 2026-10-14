class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i, j):
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j
            if (i, j) in memo:
                return memo[(i, j)]

            
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return dfs(i + 1, j + 1)
            else:
                insert = 1 + dfs(i, j + 1)
                delete = 1 + dfs(i + 1, j)
                replace = 1 + dfs(i + 1, j + 1)

                memo[(i, j)] = min(insert, delete, replace)
                return min(insert, delete, replace)
        
        return dfs(0, 0)
            
