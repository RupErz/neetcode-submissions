class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time : O ( 2 ^n * n )
        # Space : O( n )
        res = []
        subset = []

        def dfs(i) : # i is the index we currently visit
            if i >= len(nums) : # out of bounds
                res.append(subset.copy())
                return 
            
            # 1st choice : add 
            subset.append(nums[i])
            dfs(i + 1)

            # 2nd choice : don't add
            subset.pop()    
            dfs(i + 1)
        dfs(0)
        return res