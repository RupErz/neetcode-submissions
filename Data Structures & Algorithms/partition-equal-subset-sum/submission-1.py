class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 1st : Brute Force (2 ^ n)
        totalSum = sum(nums)

        def dfs(i, curSum):
            if i not in range(len(nums)):
                return False
            if totalSum == curSum * 2:
                return True

            # Take
            if dfs(i + 1, curSum + nums[i]) or dfs(i + 1, curSum):
                return True

            
            
            return False
        return dfs(0, 0)
            