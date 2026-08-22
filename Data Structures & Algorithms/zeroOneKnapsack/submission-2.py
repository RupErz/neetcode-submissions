class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity + 1
        dp = [[0] * (M) for _ in range(N)]

        # Fill the first row 
        for c in range(M):
            if c >= weight[0]:
                dp[0][c] = profit[0]

        for r in range(1, N):
            for c in range(1, M):
                skip = dp[r - 1][c]
                include = 0 
                if c >= weight[r]:
                    include = profit[r] + dp[r - 1][c - weight[r]]
                dp[r][c] = max(skip, include)
        return dp[N - 1][M - 1]