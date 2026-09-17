class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        curMin = nums[0]
        curMax = nums[0]
        cur = 1
        result = float("-inf")

        for i in range(1, len(nums)):
            cur = nums[i]
            upMin = min(cur, curMax * cur, curMin * cur)
            upMax = max(cur, curMax * cur, curMin * cur) 
            curMin = upMin
            curMax = upMax

            result = max(result, curMax)

        return result