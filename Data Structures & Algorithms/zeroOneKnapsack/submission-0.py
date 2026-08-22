class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.dfs(0, capacity, profit, weight)

    def dfs(self, i, capacity, profit, weight):
        # Base case:
        if i == len(weight):
            return 0

        # If we skip current index  
        maxProfit = self.dfs(i + 1, capacity, profit, weight)

        # If we choose current index
        newCap = capacity - weight[i]
        if newCap >= 0 :
            p = profit[i] + self.dfs(i + 1, newCap, profit, weight)
            maxProfit = max(maxProfit, p)
        
        return maxProfit

        
            


