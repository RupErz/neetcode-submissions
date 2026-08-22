class Solution:
    def jump(self, nums: List[int]) -> int:
        # Optimal : Greedy 
        l, r = 0, 0
        result = 0

        while r < len(nums) - 1:
            furthest = r
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l = r + 1
            r = furthest
            result += 1
        
        return result

        # Brute Force (DFS)
        # Time Complexity: O(k^n) k: avg jump from an idx, n = len(nums)
        # memo = {}
        # def dfs(i): # i: current idx 
        #     if i == len(nums) - 1:
        #         return 0
            
        #     if i >= len(nums):
        #         return float("inf")
            
        #     if i in memo:
        #         return memo[i]
            
        #     result = float("inf")

        #     for j in range(1, nums[i] + 1):
        #         count = 1 + dfs(i + j)

        #         if count != float("inf"):
        #             result = min(result, count)
            
        #     memo[i] = result
        #     return result
        # return dfs(0)
        
        