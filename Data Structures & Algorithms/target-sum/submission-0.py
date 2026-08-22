class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        def dfs(i, a):
            if i == len(nums):
                if a == target:
                    return 1
                else :
                    return 0
            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i + 1, a + nums[i]) + dfs(i + 1, a - nums[i])
            return cache[(i, a)]
        return dfs(0, 0)


        
        