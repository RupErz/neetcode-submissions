class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        # cache = set()
        # Optimal Sol: Will revisit a cell twice but prevent recompute
        # cache = [ [-1] * (COLS) for _ in range(ROWS)]
        visit = set()

        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS) 
                or grid[r][c] == 1 or (r, c) in visit) :
                return 0

            if (r == ROWS - 1 and c == COLS - 1):
                return 1

            # We already visit this and compute total way at this pos
            # if cache[r][c] != -1:
            #     return cache[r][c]

            visit.add((r, c))
            total = 0
            for dr, dc in directions:
                total += dfs(r + dr, c + dc)

            # cache[r][c] = total
            visit.remove((r, c))
            return total

        return dfs(0, 0)