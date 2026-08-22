class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(r, c, v):
            nonlocal count
            if r == ROWS - 1 and c == COLS - 1:
                count += 1
                return

            v.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    grid[nr][nc] == 0 and (nr, nc) not in v):
                    dfs(nr, nc, v)
            v.remove((r, c))
        
        dfs(0, 0, set())
        return count