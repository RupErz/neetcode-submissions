class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []

        while left < right and top < bottom :

            # Moving from left to right 
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Moving from top to bottom 
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # Prevent revisit if there are no rows / cols to traverse
            # e.g: [[ 1, 2, 3]] : run it by urself
            if not (left < right and top < bottom):
                break

            # Moving from right to left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Moving from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
        
            