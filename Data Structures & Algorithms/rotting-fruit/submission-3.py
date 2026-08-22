class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()
        time = 0
        total = 0
        # Finding every rotten fruit path.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    total += 1
                elif grid[r][c] == 1:
                    total += 1

        while q:
            for i in range(len(q)) :
                r, c = q.popleft()
                visit.add((r, c))
                for dr, dc in directions :
                    rotRow, rotCol = r + dr, c + dc
                    if (rotRow in range(ROWS) and rotCol in range(COLS)
                    and (rotRow, rotCol) not in visit
                    and grid[rotRow][rotCol] == 1) :
                        q.append([rotRow, rotCol])
                        visit.add((rotRow, rotCol)) 
            if q:
                time += 1
        return time if len(visit) == total else -1

        