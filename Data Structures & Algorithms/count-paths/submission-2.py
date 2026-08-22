class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # Top Down (Memoization)
        # ROWS = m
        # COLS = n
        # cache = [[0] * COLS for r in range(ROWS)]
        # def topDown(r, c, cache):
        #     if r not in range(ROWS) or c not in range(COLS):
        #         return 0
            
        #     if cache[r][c] > 0:
        #         return cache[r][c]

        #     if r == ROWS - 1 and c == COLS - 1:
        #         return 1

        #     cache[r][c] = (topDown(r, c + 1, cache) +
        #                     topDown(r + 1, c, cache))
            
        #     return cache[r][c]
        # return topDown(0, 0, cache)

        # Bottom up: 
        prevRow = [0] * n

        for r in range(m - 1, -1, -1):
            curRow = [0] * n
            curRow[-1] = 1 # Since from last position to bot right is only 1w
            for c in range(n - 2, -1, -1):
                curRow[c] = prevRow[c] + curRow[c + 1]
            prevRow = curRow
        return prevRow[0]
            