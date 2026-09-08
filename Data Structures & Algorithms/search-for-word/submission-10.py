class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != word[i] or (r, c) in visited:
                return False

            visited.add((r, c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    return True
            visited.remove((r, c))
            return False 
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False
        


