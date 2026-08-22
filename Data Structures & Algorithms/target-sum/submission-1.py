class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # dp[0][0] = 0 : at index 0 (with 0 elements to achieve amt 0 we have
        # 0 way )
        dp = [ defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1 # This is the default
        # With 0 ele chose, to get amt 0 we need 1 way

        for i in range(len(nums)):
            for amt, count in dp[i].items():
                dp[i + 1][amt + nums[i]] += count
                dp[i + 1][amt - nums[i]] += count
        return dp[len(nums)][target]

        