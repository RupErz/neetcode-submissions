class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # Bottoms up : Go from amount 0 to amount target
        # dp[0][0] = 0 : at index 0 (with 0 elements to achieve amt 0 we have
        # 0 way )
        dp = defaultdict(int)

        dp[0] = 1 # This is the default
        # With amount of 0 we have 1 choice

        for i in range(len(nums)):
            newDP = defaultdict(int)
            for amt, count in dp.items():
                newDP[amt + nums[i]] += count
                newDP[amt - nums[i]] += count
            dp = newDP
        return dp[target]


        