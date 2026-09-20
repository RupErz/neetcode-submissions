class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # visited = {}
        # def dfs(i, total):
        #     if i >= len(coins) or total > amount:
        #         return 0
        #     if total == amount:
        #         return 1
        #     if (i, total) in visited:
        #         return visited[(i, total)]

        #     # Pick or not pick, pick = stay, not pick = move
        #     pick = dfs(i, total + coins[i])

        #     skip = dfs(i + 1, total)

        #     visited[(i, total)] = pick + skip
        #     return (pick + skip)
        
        # return dfs(0, 0)

        # Bottom up
        dp = [0] * (amount + 1)
        dp[0] = 1 # At amount 0 there is only 1 way
        
        for num in coins:
            for i in range(1, amount + 1):
            # With amount i, we will pick coins that <= its val
                if num <= i:
                    dp[i] += dp[i - num]
        
        return dp[amount]

        
