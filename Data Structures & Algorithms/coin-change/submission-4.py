class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Finding path or combinations (DFS or bottom up)

        visited = {}
        def dfs(i, total):
            if i >= len(coins) or total > amount:
                return float("inf")
            if total == amount:
                return 0
            if (i, total) in visited:
                return visited[(i, total)]

            # Either pick this coin or move forward
            # Pick the coin
            pick = 1 + dfs(i, coins[i] + total)

            # Not pick this coin
            notpick = dfs(i + 1, total)

            visited[(i, total)] = min(pick, notpick)
            return visited[(i, total)]

        
        res = dfs(0, 0) 
        return res if res != float("inf") else -1
        


