class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # # Creating a 2D with extra length and val 0 each
        # dp = [ [ 0 for c in range(len(text2) + 1)] for r in range(len(text1) + 1)]

        # for r in range(len(text1) - 1, -1, -1):
        #     for c in range(len(text2) - 1, -1, -1):
        #         if text1[r] == text2[c]:
        #             dp[r][c] = 1 + dp[r + 1][c + 1]
        #         else :
        #             dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
        # return dp[0][0]
        # # Time : O(m * n) , Bottoms up
        # # Space : O(m * n)

        # Top Down :
        # To reused computed cell if necessary 
        memo = {}

        def dfs(i, j):
            if (i == len(text1) or j == len(text2)):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
            else :
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return memo[(i, j)]
        return dfs(0, 0)

