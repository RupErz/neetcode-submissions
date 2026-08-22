class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        L = 0
        totalSum = 0
        for R in range(len(nums)):
            totalSum += nums[R]
            while totalSum >= target:
                length = min(length, R - L + 1)
                totalSum -= nums[L]
                L += 1
        return length if length != float("inf") else 0
        