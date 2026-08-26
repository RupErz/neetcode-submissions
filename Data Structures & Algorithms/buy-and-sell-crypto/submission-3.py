class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy Sell
        # Buy < Sell : Maximize profits

        # 2 ptrs
        # i 10 1
        # j 1 5 6 7 1
        # 4 5 6 0
        buy, sell = 0, 0
        profit = 0

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            profit = max(profit, prices[sell] - prices[buy])
            sell += 1

        return profit 