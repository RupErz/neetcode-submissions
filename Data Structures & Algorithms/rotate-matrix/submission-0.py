class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r :
            top, bottom = l, r
            for i in range(r - l):

                # Store top left val temp into a var
                # We try to minimize temp variable by goin counterclock
                topLeft = matrix[top][l + i]

                # Store bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Store bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Store top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Store temp back into top right
                matrix[top + i][r] = topLeft
            l, r = l + 1, r - 1
        