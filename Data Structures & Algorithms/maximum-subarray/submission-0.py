class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = max(nums)
        curSum = nums[0]
        for i in range(1, len(nums)):
            # We reset our curSum if we even reach negative sum
            curSum = max(curSum, 0)
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum