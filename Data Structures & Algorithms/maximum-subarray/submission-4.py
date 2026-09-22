class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dfs at each index - Include or Start new 
        # Sliding window - > nah cause even the sum drop we cannot shrink

        result = float("-inf")
        prev = float("-inf")

        for n in nums:
            cur = max(n, n + prev)
            prev = cur

            result = max(result, cur)
        
        return result
