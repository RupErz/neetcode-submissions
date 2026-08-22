class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)
        for i in range(len(profit)):
            newDp = [0] * (capacity + 1)
            for j in range(capacity + 1):
                newDp[j] = dp[j]
                if j >= weight[i]:
                    include = profit[i] + newDp[j - weight[i]]
                    newDp[j] = max(newDp[j], include)
            dp = newDp
        return dp[capacity]