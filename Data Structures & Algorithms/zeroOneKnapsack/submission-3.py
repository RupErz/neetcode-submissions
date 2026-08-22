class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity + 1
        dp = [ 0 for _ in range(M) ]

        # Fill the first row 
        for c in range(M):
            if c >= weight[0]:
                dp[c] = profit[0]

        for r in range(1, N):
            curDp = [ 0 for _ in range(M) ]
            for c in range(1, M):
                skip = dp[c]
                include = 0 
                if c >= weight[r]:
                    include = profit[r] + dp[c - weight[r]]
                curDp[c] = max(skip, include)
            dp = curDp
        return dp[M - 1]