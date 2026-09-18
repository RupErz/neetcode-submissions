class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dfs 
        # branch solution: Have first number or not have first number


        # Include or Not include
        # i current idx, j last added idx
        visited = {}
        def dfs(i, j): 
            if i == len(nums):
                return 0

            if (i, j) in visited:
                return visited[(i, j)]
            
            # If include i then next one must be specifically larger
            include, notinclude = 0, 0
            if j == -1:
                include = 1 + dfs(i + 1, i)
            else:
                if nums[i] > nums[j]:
                    include = 1 + dfs(i + 1, i)
            
            # If skip then we just move forward j stay still
            notinclude = dfs(i + 1, j)

            visited[(i, j)] = max(include, notinclude)
            return max(include, notinclude)

        return dfs(0, -1)

