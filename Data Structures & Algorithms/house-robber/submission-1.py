class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        for i in range(len(nums) - 3, -1, -1):
            nums[i] += max(nums[i + 2:])
        return max(nums)