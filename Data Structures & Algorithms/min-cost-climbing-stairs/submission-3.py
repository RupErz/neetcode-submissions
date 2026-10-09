class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # visited = {}
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0

        #     if i in visited:
        #         return visited[i]

        #     # Make 1 step
        #     one_step = cost[i] + dfs(i + 1)

        #     # Make 2 step 
        #     two_step = cost[i] + dfs(i + 2)
        
        #     visited[i] = min(one_step, two_step)
        #     return min(one_step, two_step)
            
        # return min(dfs(0), dfs(1))

        # Dp Bottom up
        # Start from sth obvious
        n = len(cost)
        dp = [-1] * (n + 2)
        dp[n], dp[n + 1] = 0, 0 #take 0 cost to get to goal from this

        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])
        