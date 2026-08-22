class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 1st : Brute Force (2 ^ n)
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        target = totalSum // 2

        memo = {}

        def dfs(i, curSum):
            if i not in range(len(nums)) or curSum > target:
                return False
            if curSum == target:
                return True
            if (i, curSum) in memo:
                return memo[(i, curSum)]

            # Take
            memo[(i, curSum)] = dfs(i + 1, curSum + nums[i]) or dfs(i + 1, curSum)
            
            return memo[(i, curSum)]
        return dfs(0, 0)
            