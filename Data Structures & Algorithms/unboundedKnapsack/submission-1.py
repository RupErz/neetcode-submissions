class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = [ [-1] * (capacity + 1) for _ in range(len(weight)) ]
        return self.dfs(0, profit, weight, capacity, cache)
    
    def dfs(self, index, profit, weight, curCap, cache):
        # Base case : 
        if index == len(weight):
            return 0

        # Memoization 
        if cache[index][curCap] != -1:
            return cache[index][curCap]

        # Not choose ( Later path cannot reuse the number )
        maxProfit = self.dfs(index + 1, profit, weight, curCap, cache)

        # Choose ( Later path can still reuse the number )
        newCap = curCap - weight[index]
        if newCap >= 0:
            newMaxProfit = profit[index] + self.dfs(index, profit, weight, newCap, cache)
            maxProfit = max(maxProfit, newMaxProfit)
        cache[index][curCap] = maxProfit
        return maxProfit

        # If no optimization : 2^n
        # Optimization : 2D array = size array = n * m  , Space : n * m