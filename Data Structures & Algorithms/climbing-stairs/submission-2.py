class Solution:
    def climbStairs(self, n: int) -> int:
        # Climb 1 to 2 steps at a time ~= Fibonacci Sequence (n-1)+(n-2)

        # Bottoms up
        if n <= 1:
            return 1
        
        dp = [1, 1] # take 1 step to reach either 0 or 1 stair
        i = 2
        while i <= n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i += 1
        return dp[1]