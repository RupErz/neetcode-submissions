class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i, cache):
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]

            # If we rob
            rob = nums[i] + dfs(i + 2, cache)
                
            # If we skip
            skip = dfs(i + 1 , cache)
        
            cache[i] = max(skip, rob)
            return cache[i]
        return dfs(0, cache)