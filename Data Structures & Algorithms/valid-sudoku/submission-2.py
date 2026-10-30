class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 0 1 2 3 4 5 6 7 8
        rows = {i: set() for i in range(len(board))}
        cols = {i: set() for i in range(len(board[0]))}
        sub = {}
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r // 3, c // 3) not in sub:
                    sub[(r // 3, c // 3)] = set()


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                curNum = board[r][c]
                if curNum in rows[r] or curNum in cols[c] or curNum in sub[(r // 3, c // 3)]:
                    return False
                rows[r].add(curNum)
                cols[c].add(curNum)
                sub[(r // 3, c // 3)].add(curNum)
        return True

