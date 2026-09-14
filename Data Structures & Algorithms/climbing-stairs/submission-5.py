class Solution:
    def climbStairs(self, n: int) -> int:
        
        # 1 or 2 step
        # record = {}
        # def dfs(i):
        #     if i > n:
        #         return 0
        #     if i == n:
        #         return 1
        #     if i in record:
        #         return record[i]

        #     result = 0
        #     # Take 1 step
        #     result += dfs(i + 1)

        #     # Take 2 step
        #     result += dfs(i + 2)

        #     record[i] = result
        #     return result
        
        # return dfs(0)

        if n == 1:
            return 1
        # f(0) = 1, f(1) = 1
        dp = [1, 1] # [at 0, at 1] -> [at 1, at 2]
        i = 1

        while i < n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i += 1

        return dp[1]
