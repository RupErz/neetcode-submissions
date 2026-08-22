class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}

        def dfs(i, amt):
            if i >= len(coins) or amt < 0:
                return 0
            if amt == 0:
                return 1

            if (i, amt) in cache:
                return cache[(i, amt)]

            # 2 Choices: We pick current coin or skip to the next coin
            cache[(i, amt)] = dfs(i, amt - coins[i]) + dfs(i + 1, amt)
            return cache[(i, amt)]
        return dfs(0, amount)

       