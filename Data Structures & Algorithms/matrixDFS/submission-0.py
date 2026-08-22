class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        cache = set()

        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS) 
                or grid[r][c] == 1 or (r, c) in cache) :
                return 0

            if (r == ROWS - 1 and c == COLS - 1):
                return 1

            total = 0
            cache.add((r, c))
            for dr, dc in directions:
                total += dfs(r + dr, c + dc)

            cache.remove((r, c))
            return total

        return dfs(0, 0)