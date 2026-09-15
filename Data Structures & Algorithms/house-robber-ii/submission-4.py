class Solution:
    def rob(self, nums: List[int]) -> int:
        # Only care about when you rob for the last house before cycle
        if len(nums) == 1:
            return nums[0]

        record = {}
        def dfs(i, stop):
            if i > stop:
                return 0

            if (i, stop) in record:
                return record[(i, stop)]
            
            result = max(nums[i] + dfs(i + 2, stop), dfs(i + 1, stop))
            record[(i, stop)] = result
            return result
        

        result = max(dfs(0, len(nums) - 2), dfs(1, len(nums) - 1))
        return result