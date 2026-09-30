class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, diag, antidiag = set(), set(), set()
        result = []

        board = [['.']*(n) for i in range(n)]
        def dfs(r):
            if r == n :
                result.append([''.join(row) for row in board])
                return 
            
            for c in range(n):
                if c in cols or (r - c) in diag or (r + c) in antidiag:
                    continue
                
                # Place
                cols.add(c)
                diag.add(r - c)
                antidiag.add(r + c)
                board[r][c] = 'Q'
                dfs(r + 1)

                # Unplace
                cols.remove(c)
                diag.remove(r - c)
                antidiag.remove(r + c)
                board[r][c] = '.'

        dfs(0)
        return result
