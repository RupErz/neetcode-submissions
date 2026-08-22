class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        return res