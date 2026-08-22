class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(boxGrid), len(boxGrid[0])

        # Since every time we rotate 90, rows turn columns
        # So we need to loop for each row and adjust the gravity on it
        # Row by Row
        for r in range(ROWS):
            i = COLS - 1
            for c in range(COLS - 1, -1, -1):
                if boxGrid[r][c] == "#":
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                    i -= 1
                elif boxGrid[r][c] == "*":
                    i = c - 1
        
        # Rotate the box
        res = []

        for c in range(COLS):
            col = []
            for r in range(ROWS - 1, -1, -1):
                col.append(boxGrid[r][c])
            res.append(col)

        return res
        

