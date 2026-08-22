class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            newDP = [0] * (amount + 1)
            newDP[0] = 1
            for a in range(1, amount + 1, 1):
                newDP[a] = dp[a]
                if (a - c) >= 0 :
                    newDP[a] += newDP[a - c]
            dp = newDP # Only work in Python 
        return dp[amount]