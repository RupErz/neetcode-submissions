class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Result have to be the entire list 
        # Avoid Duplication 

        # Pick or Not Pick
            # Pick: + or - 
        # Not Pick: just move up
        visited = {}
        def dfs(i, total):
            if total == target and i == len(nums):
                return 1 
            if i >= len(nums):
                return 0
            
            if (i, total) in visited:
                return visited[(i, total)]
            # Pick
                # add = dfs(i + 1, total + nums[i])
                # subtract = dfs(i + 1, total - nums[i])
            add = dfs(i + 1, total + nums[i])
            # Not pick 
                # skip = dfs(i + 1, total)
            subtract = dfs(i + 1, total - nums[i])


            visited[(i, total)] = add + subtract
            return (add + subtract)
        return dfs(0, 0)
        # [1, 4]. target = 5

