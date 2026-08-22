class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        result = 0
        visit = set()

        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS)
                or (r, c) in visit or grid[r][c] == '0'):
                return 

            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    dfs(r, c)
                    result += 1
        return result 
            