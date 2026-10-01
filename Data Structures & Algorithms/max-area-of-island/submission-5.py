class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0 :
                return 0
            
            area = 1
            # Capture this current spot
            grid[r][c] = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)

            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    result = max(result, dfs(r, c))
        
        return result 
