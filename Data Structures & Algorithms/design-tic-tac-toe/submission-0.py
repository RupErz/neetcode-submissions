class TicTacToe:
    # 1. Creating a n * n matrices 
    # 2. Everytime player move we will mark the cell with the corresponding id
    # 3. How do we decide when whoever win ?
    # horizontal, vertical, or diagonal 
    # dfs ? 
    # whenever we mark a spot, we will explore every possible path from it to check?
    
    def __init__(self, n: int):
        self.matrix = [[0] * n for r in range(n)]
        self.ROWS = n
        self.COLS = n

        # Tracking counts of 2 player in hashmap
        self.rowsCount = { i + 1 : { r:0 for r in range(n)}  for i in range(2) }
        self.colsCount = { i + 1 : { c:0 for c in range(n)} for i in range(2)}
        self.diagonal = { i + 1 : 0 for i in range(2)}
        self.antidiagonal = { i + 1 : 0 for i in range(2)}

    def move(self, row: int, col: int, player: int) -> int:
        # No need dfs, count or keep track the counts on the line relate to it
        # rows (rows number)
        # cols (cols number)
        # left to right diagonal (when r + c = n - 1)
        # right to left diagonal (when r = c)
        # So we always have to check rows and cols
        # 2 diagonals is situational as long as the condition is satisfied
        # counting everytime user move is redundant so to optimize we need to track it !
        
        # Mark this current cell
        self.matrix[row][col] = player

        # Check for every possible cases
        if self.rowsCount[player][row] + 1 == self.ROWS:
            return player
        else:
            self.rowsCount[player][row] += 1

        if self.colsCount[player][col] + 1 == self.COLS:
            return player
        else:
            self.colsCount[player][col] += 1

        if row == col: # This a valid diagonal cell
            if self.diagonal[player] + 1 == self.ROWS:
                return player
            else:
                self.diagonal[player] += 1

        if row + col == self.ROWS - 1:
            if self.antidiagonal[player] + 1 == self.ROWS:
                return player
            else:
                self.antidiagonal[player] += 1
        
        return 0
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
