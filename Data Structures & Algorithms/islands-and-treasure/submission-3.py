class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        zeros = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    zeros.appendleft((r, c))
                    visited.add((r, c))
        
        level = 1
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        while zeros:
            for i in range(len(zeros)):
                neiR, neiC = zeros.pop()
                # Add its neighbor
                for dr, dc in directions:
                    if (neiR + dr) in range(ROWS) and (neiC + dc) in range(COLS) and grid[neiR + dr][neiC + dc] != -1 and (neiR + dr, neiC + dc) not in visited:
                        # Add it then assign level
                        visited.add((neiR + dr, neiC + dc))
                        zeros.appendleft((neiR + dr, neiC + dc))
                        grid[neiR + dr][neiC + dc] = level 
            level += 1
        
                    

