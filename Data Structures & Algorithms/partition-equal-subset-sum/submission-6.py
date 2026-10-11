class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        def dfs(i, total):
            if i >= len(nums) or total > target:
                return False
            
            if total == target:
                return True
            
            # Pick or Skip
            return (dfs(i + 1, total + nums[i]) or dfs(i + 1, total))
        
        return dfs(0, 0)