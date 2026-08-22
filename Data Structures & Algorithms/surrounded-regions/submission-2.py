class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def capture(r, c):
            if (r not in range(ROWS) or c not in range(COLS)
                or board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            for dr, dc in directions :
                newR, newC = r + dr, c + dc
                capture(newR, newC)
        #Phase 1 : DFS Capture unsurrounded region ( O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if( board[r][c] == 'O' and 
                    (r in [0, ROWS - 1] or
                    c in [0, COLS - 1])) :
                    capture(r, c)

        #Phase 2: For Loop Capture surrounded region , simply mark O (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        #Phase 3: For Loop Uncapture unsurrounded region (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
            