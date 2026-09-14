class Solution:
    def rob(self, nums: List[int]) -> int:
        # Rob or not Rob
        # record = {}
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if i in record:
        #         return record[i]
        #     # So we have 2 choices at first
        #     # Either skip or rob first house and that will determine the outcome
        #     result = float('inf')
            
        #     rob = nums[i] + dfs(i + 2)
        #     norob = dfs(i + 1)

        #     result = max(rob, norob)
        #     record[i] = result

        #     return result

        
        # return dfs(0)
        if len(nums) == 1:
            return nums[0]

        dp = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len(nums):
            tmp = dp[1]
            dp[1] = max(dp[0] + nums[i], dp[1])
            dp[0] = tmp
            i += 1

        return max(dp[0], dp[1])
