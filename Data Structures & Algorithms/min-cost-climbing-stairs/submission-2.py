class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        visited = {}
        def dfs(i):
            if i >= len(cost):
                return 0

            if i in visited:
                return visited[i]
                
            # Make 1 step
            one_step = cost[i] + dfs(i + 1)

            # Make 2 step 
            two_step = cost[i] + dfs(i + 2)
        
            visited[i] = min(one_step, two_step)
            return min(one_step, two_step)
            
        return min(dfs(0), dfs(1))