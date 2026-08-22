class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # DP 
        dp = [0] * (amount + 1)
        dp[0] = 1

        for r in range(len(coins)):
            newDp = [0] * (amount + 1)
            newDp[0] = 1
            for c in range(1, amount + 1):
                newDp[c] = dp[c]
                # If we can use the current coin 
                if c >= coins[r]:
                    newDp[c] += newDp[c - coins[r]]
            dp = newDp
        return dp[amount]
