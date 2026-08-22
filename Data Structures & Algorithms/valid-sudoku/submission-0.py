class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Using hash to track every rows , cols with the duplicate
        # Unique => Set
        hashcol = defaultdict(set) #Coming from package : collections.
        hashrow = defaultdict(set)
        hashgrid = defaultdict(set) #Key is a set (a // 3 , b // 3) Value is a set

        # Looping order : row -> col 
        for i in range(9): #9x9 row
            for j in range(9): #cols
                if board[i][j] == '.':
                    continue
                if (board[i][j] in hashcol[i]
                    or board[i][j] in hashrow[j]
                    or board[i][j] in hashgrid[(i // 3, j // 3)]):
                    return False
                hashcol[i].add(board[i][j])
                hashrow[j].add(board[i][j])
                hashgrid[(i // 3, j // 3)].add(board[i][j])
        return True