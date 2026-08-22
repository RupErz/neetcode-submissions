class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coin = 3
        # amount = 12
        # dp[12] = 1 + dp[9] #at amount 12 with coin 1 coin 3, we need 12-3  
        # 7 -> 8

        # can be Math.maxinteger , an inf so use MIN. amount + 1 is a max
        dp = [amount + 1] * (amount + 1) 
        # base case : amount is 0 need 0 coins.
        dp[0] = 0

        # DP - TopDown : Starting at amount then go down
        for a in range(1, amount + 1, 1) :
            for c in coins:
                if a - c >= 0 :
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
            # a = 4, amount 8
            # [1, 3, 5, 7] -> 4 coin =-> loop thru 4 coins
            # dp[a] = 1 + dp[1]