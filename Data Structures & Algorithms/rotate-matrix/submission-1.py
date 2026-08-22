class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        l, r = 0, len(matrix) - 1

        n = len(matrix)

        while l < r:
            # 3x3 rotate 2 groups of 4
            # 4x4 rotate 3 groups of 4
            # 5x5 rotate 4 groups of 4 => Right - Left
            for j in range(r - l):
                # Update:

                tmp = matrix[r - j][l]

                matrix[r - j][l] = matrix[r][r - j]
                matrix[r][r - j] = matrix[l + j][r]
                matrix[l + j][r] = matrix[l][l + j]
                matrix[l][l + j] = tmp

            l += 1
            r -= 1