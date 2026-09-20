class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Many paths -> DFS

        # buying: T when we can Buy stock, F when we can Sell stock
        visited = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in visited:
                return visited[(i, buying)]

            if buying:
                buy = -prices[i] + dfs(i + 1, False)
                # or skip
                skip = dfs(i + 1, True)

                visited[(i, buying)] = max(buy, skip)
                return max(buy, skip)
            else:
                sell = prices[i] + dfs(i + 2, True)
                # or skip
                skip = dfs(i + 1, False)

                visited[(i, buying)] = max(sell, skip)
                return max(sell, skip)
        return dfs(0, True)
            