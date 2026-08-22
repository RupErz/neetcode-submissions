class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # [1,1,1] [2,2,2]  
        # [1,1,0] [2,2,0]
        # [1,0,1] [2,0,1]

        # imagine like a graph, i think of DFS first
        # With a set to avoid redundancy 

        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(image), len(image[0])

        def dfs(r, c, org):
            # If we see a different color then we do nothing
            if image[r][c] != org:
                return

            visited.add((r, c))
            # Change the current color cell
            image[r][c] = color

            # Start visiting every adj cells
            for dr, dc in directions:
                curR, curC = r + dr, c + dc

                if curR in range(ROWS) and curC in range(COLS) and (curR, curC) not in visited and image[curR][curC] == org:
                    dfs(curR, curC, org)

        dfs(sr, sc, image[sr][sc])
        return image


