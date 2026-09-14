class Solution:
    def rob(self, nums: List[int]) -> int:
        # Rob or not Rob
        record = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in record:
                return record[i]
            # So we have 2 choices at first
            # Either skip or rob first house and that will determine the outcome
            result = float('inf')
            
            rob = nums[i] + dfs(i + 2)
            norob = dfs(i + 1)

            result = max(rob, norob)
            record[i] = result

            return result

        
        return dfs(0)