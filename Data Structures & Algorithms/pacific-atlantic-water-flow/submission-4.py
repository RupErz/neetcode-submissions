class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(heights), len(heights[0])


        # Pacific when: r = 0 alone or r = any but c = 0
        # Atlantic when: r = n - 1 alone or r = any but c = n - 1
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            # Stop revisit
            if (r, c) in visited:
                return 

            visited.add((r, c))
            cur_height = heights[r][c]

            # Only flow to higher or equal
            for dr, dc in directions:
                # Must check before moving
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS):
                    n_height = heights[nr][nc]
                    if n_height >= cur_height:
                        dfs(nr, nc, visited)



        # Since we dont know which position is guarantee so we have to loop every position at least once
        result = []
        # pacific region:
        # r = 0 c rand
        for c in range(COLS):
            dfs(0, c, pacific)
        for r in range(ROWS):
            dfs(r, 0, pacific)

        # Atlantic Region
        # c = n -1 or r = n -1
        for r in range(ROWS):
            dfs(r, len(heights[0]) - 1, atlantic)
        for c in range(COLS):
            dfs(len(heights) - 1, c, atlantic)

        # One more pass to check
        for r, c in pacific:
            if (r, c) in atlantic:
                result.append([r, c])
        
        return result

        