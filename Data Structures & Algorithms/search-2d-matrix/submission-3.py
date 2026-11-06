class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (r + l) // 2

            if target <= matrix[mid][-1] and target >= matrix[mid][0]:

                il, ir = 0, len(matrix[mid]) - 1
                while il <= ir:
                    imid = (il + ir) // 2

                    if target == matrix[mid][imid]:
                        return True
                    
                    if target > matrix[mid][imid]:
                        il = imid + 1
                    else:
                        ir = imid - 1
            
            if target > matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
