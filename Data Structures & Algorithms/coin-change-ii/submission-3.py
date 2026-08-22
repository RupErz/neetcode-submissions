class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i, curAmount):
            if i not in range(len(coins)) or curAmount > amount:
                return 0
            if curAmount == amount:
                return 1
            if (i, curAmount) in cache:
                return cache[(i, curAmount)]
            
            cache[(i, curAmount)] = dfs(i + 1, curAmount) + dfs(i, curAmount + coins[i])

            return cache[(i, curAmount)]
        return dfs(0, 0)