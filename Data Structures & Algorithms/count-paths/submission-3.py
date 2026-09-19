class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Top down with memo
        directions = [[0, 1], [1, 0]]
        ROWS, COLS = m, n
        visited = {}
        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS):
                return 0
            
            if r == (m - 1) and c == (n - 1):
                return 1
            if (r, c) in visited:
                return visited[(r, c)]

            total_path = 0
            for dr, dc in directions:
                total_path += dfs(r + dr, c + dc)
            

            visited[(r, c)] = total_path
            return total_path
        
        return dfs(0, 0)
