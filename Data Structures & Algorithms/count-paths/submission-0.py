class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # directions = [[1, 0], [0, 1]]
        # def dfs(row, col):
        #     if (row not in range(m)
        #         or col not in range(n)):
        #         return 0
        #     if (row == m - 1 and col == n - 1) :
        #         return 1
        #     res = 0
        #     for dr, dc in directions :
        #         res += dfs(row + dr, col + dc)
        #     return res
        # return dfs(0, 0)
    # Time : 2 choices each time we recurse => 2^(m + n)

        # Optimal : Using a cache ( Memoization in DP)
        
        # Last row always 1 choice to reach destination.
        # Last column of each row always need 1 choice to reach destination.

        # Creating last row
        row = [1] * n

        # Looping through each rows except last row
        for r in range(m - 1):
            newRow = [1] * n # last column is always 1
            # Start modifying the newRow from right to left
            for c in range(n - 2, -1, -1):
                newRow[c] = newRow[c + 1] + row[c]
            row = newRow 
        return row[0]
 