class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # How we work
        # Buy : i + 1
        # Sell : i + 2 ( due to the cooldown of 1 day after sell )

        # We will have a cache to store (key: (i, buyingState) : profit)
        dp = {}

        # i : index, buying : current state either T (r for buy) or F (sell)
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
            # We can either buy or wait for 1 more day
                buy = dfs(i + 1, False) - prices[i] # buy = lost money
                wait = dfs(i + 1, True)
                # Caching this
                dp[(i, buying)] = max(buy, wait)
            else :
            # We can either sell or wait for 1 more day
                sell = dfs(i + 2, True) + prices[i]
                wait = dfs(i + 1, False)
                dp[(i, buying)] = max(sell, wait)
            return dp[(i, buying)] # Profit at current index
        return dfs(0, True)