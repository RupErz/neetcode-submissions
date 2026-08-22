class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        maxArea = 0

        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS)
               or grid[r][c] == 0 or (r, c) in visit):
                return 0
            
            area = 1
            visit.add((r, c))
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area  


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(maxArea, dfs(r, c)) 
        return maxArea