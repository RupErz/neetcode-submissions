class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1

        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1],
        [1, -1], [-1, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = collections.deque()
        queue.append((0, 0))

        visit = set()
        visit.add((0, 0))

        result = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and nc in range(COLS)
                        and (nr, nc) not in visit and grid[nr][nc] == 0):
                        visit.add((nr, nc))
                        queue.append((nr, nc))
            result += 1
            if (ROWS - 1, COLS - 1) in visit:
                    return result
        return -1
                
