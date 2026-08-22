class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS 
        # if len(grid) <= 0 :
        #     return 0 
        # ROWS, COLS = len(grid), len(grid[0])
        # directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        # def dfs(r, c):
        #     if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0:
        #         return 0
            
        #     grid[r][c] = 0
        #     area = 1

        #     for dr, dc in directions :
        #         area += dfs(r + dr, c + dc)
        #     return area

        # max_area = 0
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1:
        #             max_area = max(max_area, dfs(r, c))
        # return max_area if len(grid) > 0 else 0

        #BFS :
        # Using a queue
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        visit = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            area = 1

            while q :
                row, col = q.popleft()
                for dr, dc in directions :
                    newRow, newCol = row + dr, col + dc
                    if (newRow in range(ROWS) and newCol in range(COLS)
                    and (newRow, newCol) not in visit 
                    and grid[newRow][newCol] == 1):
                        q.append((newRow, newCol))
                        visit.add((newRow, newCol))
                        area += 1
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, bfs(r, c))
        return max_area