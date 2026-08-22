class Solution:
    def jump(self, nums: List[int]) -> int:
        # Brute Force (DFS)

        def dfs(i): # i: current idx 
            if i == len(nums) - 1:
                return 0
            
            if i >= len(nums):
                return float("inf")
            
            result = float("inf")

            for j in range(1, nums[i] + 1):
                count = 1 + dfs(i + j)

                if count != float("inf"):
                    result = min(result, count)
            
            return result
        return dfs(0)
        
        