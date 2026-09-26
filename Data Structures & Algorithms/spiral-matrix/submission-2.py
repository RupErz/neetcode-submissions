class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, len(matrix[0])
        top = 0
        bottom = ROWS - 1
        left = 0
        right = COLS - 1
        result = []

        while top <= bottom and left <= right:
            # Top row
            for t in range(left, right + 1):
                result.append(matrix[top][t])

            # Right column
            for r in range(top + 1, bottom + 1):
                result.append(matrix[r][right])

            if top != bottom:
                # Bottom Row
                for b in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom][b])
            
            if right != left:
                # Left Row
                for l in range(bottom - 1, top, -1):
                    result.append(matrix[l][left])

            # Once we done we shrink it
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        return result
            