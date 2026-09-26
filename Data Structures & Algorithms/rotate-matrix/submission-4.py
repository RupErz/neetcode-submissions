class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        # topleft = matrix[0][0]
        # topright = matrix[0][COLS - 1]
        # botright = matrix[ROWS - 1][COLS - 1]
        # botleft = matrix[ROWS - 1][0]

        # matrix[0][0] = botleft
        # matrix[0][COLS - 1] = topleft
        # matrix[ROWS - 1][COLS - 1] = topright
        # matrix[ROWS - 1][0] = botright


        l, r = 0, COLS - 1
        # Outer layer (to shrink later)
        while l < r:
            # Inner layer
            # last one is already handle 
            for i in range(r - l):
                topleft = matrix[l][l + i]
                topright = matrix[l + i][r]
                botright = matrix[r][r - i]
                botleft = matrix[r - i][l]

                # Start moving 
                matrix[l][l + i] = botleft
                matrix[l + i][r] = topleft
                matrix[r][r - i] = topright
                matrix[r - i][l] = botright
            l += 1
            r -= 1
        




        
  



