class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #1: Only go through char in words
        #2 : Start backtrack 4 directions up down left right
        #3: Avoid dup: Using SET.
        #4 its a brute force 2 nested loop

        ROWS, COLS = len(board), len(board[0])
        path = set() # which store (row, cols) as each val

        def dfs(r, c, i) : # row, col, cur idx in word
            if i == len(word):
                return True

            if (r < 0 or c <0 or r >= ROWS or c >= COLS 
            or word[i] not in board[r][c] or (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1))
            path.remove((r, c)) # why ?
            # So whenever we at a val we explore with paths
            # into our set, if we done we should remove and make it clean
            # so we can move on to the next val
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
        # Time : m * n : dimension board * dfs()
        # dfs : O(len(word) * 4^len(word)) : callstack: lenofWord
        # => O(m*n*4^N)