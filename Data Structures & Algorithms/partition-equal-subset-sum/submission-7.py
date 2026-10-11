class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        visited = {}
        def dfs(i, total):
            if i >= len(nums) or total > target:
                return False
            
            if total == target:
                return True
            
            if (i, total) in visited:
                return visited[(i, total)]
            
            
            # Pick or Skip
            visited[(i, total)] = (dfs(i + 1, total + nums[i]) or dfs(i + 1, total))
            return visited[(i, total)]
        
        return dfs(0, 0)