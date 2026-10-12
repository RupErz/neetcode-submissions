class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        visited = {}
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if (r, c) in visited:
                return visited[(r, c)]

            total = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and matrix[nr][nc] > matrix[r][c]:
                    total = max(total, 1 + dfs(nr, nc))

            visited[(r, c)] = total
            return visited[(r, c)]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
        return max(visited.values())