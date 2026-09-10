class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        result = 0

        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or grid[r][c] == "0":
                return
            
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    result += 1
        return result 