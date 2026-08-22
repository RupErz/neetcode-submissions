class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Instead of putting 2 pointers on start and end
        #We can try put 2 ptr side by side
        # L, R : L min, R max
        l, r = 0, 1
        profit = 0
        #l : buy
        #r : sell => profit = sell - buy
        while r < len(prices):
            if prices[l] > prices[r]:
            #We can't find profit
                l = r
                r += 1
                # minLeft = min(minLeft, prices[])
            else : 
                profit = max(profit, prices[r] - prices[l])
                r += 1
        return profit


