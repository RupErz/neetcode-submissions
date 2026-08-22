class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # Dynamic Programming 
        # Min cost to paint house i with color c is equals to cost[i][c] + min(2 prev house with different color)

        n = len(costs)
        if n == 0:
            return 0
        
        dp = [[0] * 3 for i in range(n)]
        
        # Fill out the first house
        for i in range(3):
            dp[0][i] = costs[0][i]
        # houses [[2, 3, 5], [0, 0, 0]]
        # Meaning first houses min to paint with color Red is 2, Blue is 3, Green is 5
        
        for i in range(1, n):
            for c in range(3):
                dp[i][c] = (costs[i][c] + min(
                    dp[i - 1][(c + 1) % 3],
                    dp[i - 1][(c + 2) % 3]
                ))
        
        return min(dp[n - 1])