class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrixSize = len(matrix) * len(matrix[0]) # the number of number
        colNum = len(matrix[0])

        l, r = 0, matrixSize - 1
        while l <= r :
            mid = ( l + r ) // 2
            # mid = l + ((r - l) // 2) integer overflow
            row = mid // colNum
            col = mid - row * colNum
            if matrix[row][col] < target : #Each row has 4 columns
                l = mid + 1
            elif matrix[row][col] > target :
                r = mid - 1
            else:
                return True
        return False
