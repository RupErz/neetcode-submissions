class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
            ROWS, COLS = len(matrix), len(matrix[0])
            rowszero, colszero = set(), set()

            # Traverse thru to see which rows and cols need to mark 0 
            for r in range(ROWS):
                for c in range(COLS):
                    if matrix[r][c] == 0:
                        rowszero.add(r)
                        colszero.add(c)

            # After we know which rows / cols need to be marked zero then
            for r in range(ROWS):
                for c in range(COLS):
                    if r in rowszero or c in colszero:
                        matrix[r][c] = 0
            
            

