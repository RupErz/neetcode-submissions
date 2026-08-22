class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # We loop through 2D like usual
        # We need a fcn to check at current spot, it's valid or not
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def backtrack (r, c, i):
            if i == len(word):
                return True
            # False when: outOfBounds,not relate to words, duplication
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or (r, c) in path :
                return False
            
            path.add((r, c))
            result = (backtrack(r + 1, c, i + 1) or
                    backtrack(r - 1, c, i + 1) or
                    backtrack(r, c + 1, i + 1) or
                    backtrack(r, c - 1, i + 1) )
            path.remove((r, c))
            return result
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False
        # Time : m * n * 4^(len(word))