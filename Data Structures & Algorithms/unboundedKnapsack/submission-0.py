class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.dfs(0, profit, weight, capacity)
    
    def dfs(self, index, profit, weight, curCap):
        # Base case : 
        if index == len(weight):
            return 0

        # Not choose ( Later path cannot reuse the number )
        maxProfit = self.dfs(index + 1, profit, weight, curCap)

        # Choose ( Later path can still reuse the number )
        newCap = curCap - weight[index]
        if newCap >= 0:
            newMaxProfit = profit[index] + self.dfs(index, profit, weight, newCap)
            maxProfit = max(maxProfit, newMaxProfit)
        return maxProfit