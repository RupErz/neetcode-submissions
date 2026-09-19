class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # text 1 = row, text 2 = col
        # Top Down
        # topdown = [[0] * len(text2) for r in range(len(text1))]
        # ROWS, COLS = len(text1), len(text2)

        # # Start at the top we traverse down 
        # visited = {}
        # def dfs(r, c):
        #     if r not in range(ROWS) or c not in range(COLS):
        #         return 0
        #     if (r, c) in visited:
        #         return visited[(r, c)]
        #     # Compare 2 character:
        #     longest = 0
        #     if text1[r] == text2[c]:
        #         # Move diagonally 
        #         longest = 1 + dfs(r + 1, c + 1)
        #     else:
        #         longest = max(dfs(r + 1, c), dfs(r, c + 1))
        #     visited[(r, c)] = longest    

        #     return longest 
        
        # return dfs(0, 0)

        # Bottom up:
        dp = [[0] * (len(text2) + 1) for r in range(len(text1) + 1)]

        for r in range(len(text1) - 1, -1, -1):
            for c in range(len(text2) - 1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
        
        return dp[0][0]
                

