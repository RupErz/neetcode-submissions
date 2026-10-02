class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [1,0], [0, -1], [-1, 0]]

        def dfs(r, c):
            if board[r][c] == "X":
                return

            board[r][c] = "#"

            for dr, dc in directions:
                if r + dr in range(ROWS) and c + dc in range(COLS) and board[r + dr][c + dc] != "#":
                    dfs(r + dr, c + dc)
        
        # Traverse around the edge
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS -1 or c == 0 or c == COLS - 1) and board[r][c] == "O":
                    dfs(r, c)
                
        # Start capturing the unsafe one
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "#":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"

                   
            
