class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Assume: 
        # i -> idx of string i
        # j -> idx of string j
        # If they are match 
        # => LCS = [i + 1:] + 1 (first match letter)
        # If they not match
        # => LCS = ([i + 1:] and [j:]) OR ([i:] and [j + 1:])
        # Code : Bottom up, 2D DP, match = go diagonal

        # Make an extra row, col default as 0
        ROWS, COLS = len(text2), len(text1)
        dp = [ [0] * (len(text1) + 1) for r in range(len(text2) + 1)]

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if text2[r] == text1[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
        return dp[0][0]
                


             