class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # A deque storing (row, column, level)
        # append and popleft
        q = collections.deque([(0, 0, 0)])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        # Initialize set with first val
        visit = set()
        visit.add((0, 0))

        while q:
            for i in range(len(q)):
                r, c, level = q.popleft()

                if (r == ROWS - 1 and c == COLS - 1):
                    return level

                # if (grid[r][c] == 1 or r not in range(ROWS)
                #     or c not in range(COLS) or (r, c) in visit):
                for dr, dc in directions:
                    newRow, newCol = r + dr, c + dc
                    if (newRow in range(ROWS) and newCol in range(COLS) and
                        grid[newRow][newCol] != 1 and (newRow, newCol) not in visit):
                        visit.add((newRow, newCol))
                        q.append((newRow, newCol, level + 1))
        return -1
                        




