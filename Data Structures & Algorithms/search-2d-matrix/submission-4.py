class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # l, r = 0, len(matrix) - 1
        # while l <= r:
        #     mid = (r + l) // 2

        #     if target <= matrix[mid][-1] and target >= matrix[mid][0]:

        #         il, ir = 0, len(matrix[mid]) - 1
        #         while il <= ir:
        #             imid = (il + ir) // 2

        #             if target == matrix[mid][imid]:
        #                 return True
                    
        #             if target > matrix[mid][imid]:
        #                 il = imid + 1
        #             else:
        #                 ir = imid - 1
        #         return False
            
        #     if target > matrix[mid][-1]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        
        # return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = (l + r) // 2

            rows = mid // n
            cols = mid % n

            if matrix[rows][cols] == target:
                return True
            
            if matrix[rows][cols] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

