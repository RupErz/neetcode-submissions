class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = [[-1] * (capacity + 1) for _ in range(len(weight))]
        return self.dfs(0, capacity, profit, weight, cache)

    def dfs(self, i, capacity, profit, weight, cache):
        # Base case:
        if i == len(weight):
            return 0

        # Checking for cache
        if cache[i][capacity] != -1:
            return cache[i][capacity]

        # If we skip current index  
        maxProfit = self.dfs(i + 1, capacity, profit, weight, cache)

        # If we choose current index
        newCap = capacity - weight[i]
        if newCap >= 0 :
            p = profit[i] + self.dfs(i + 1, newCap, profit, weight, cache)
            maxProfit = max(maxProfit, p)
        
        # Store into our cache
        cache[i][capacity] = maxProfit

        return maxProfit

        
            


