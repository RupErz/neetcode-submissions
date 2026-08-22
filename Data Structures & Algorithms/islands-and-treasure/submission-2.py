class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #BFS : 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 :
                    q.append((r, c))
        level = 1
        while q:
            for t in range(len(q)):
                row, col = q.popleft()
                visit.add((row, col))
                for dr, dc in directions :
                    newRow, newCol = row + dr, col + dc
                    if (newRow in range(ROWS) and newCol in range(COLS)
                    and (newRow, newCol) not in visit
                    and grid[newRow][newCol] > 0):
                        grid[newRow][newCol] = level 
                        visit.add((newRow, newCol))
                        q.append((newRow, newCol))
            level += 1
    # Time : (Rows * Cols)
    # Since the BFS part dominate the entire algorithm
    # We add and pop each node at most 1 in order to process ( R * C )
    # Within each node, we visit up to 4 neighbors => ( 4 * R * C )
    # In total we have : O(R * C)


                