class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS 
        if len(grid) <= 0 :
            return 0 
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1

            for dr, dc in directions :
                area += dfs(r + dr, c + dc)
            return area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area if len(grid) > 0 else 0