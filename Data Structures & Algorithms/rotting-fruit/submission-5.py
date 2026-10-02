class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rotted = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotted.appendleft((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Start rotting everything surround it
        minutes = 0
        while rotted:
            if fresh == 0:
                break
            for i in range(len(rotted)):
                rr, rc = rotted.pop()

                for dr, dc in directions:
                    nr, nc = rr + dr, rc + dc
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        rotted.appendleft((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1


