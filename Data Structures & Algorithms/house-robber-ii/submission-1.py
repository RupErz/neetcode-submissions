class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxRob(nums):
            rob1, rob2 = 0, 0
            for i in nums :
                tmp = max(i + rob1, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
        return max(maxRob(nums[:(len(nums) - 1)]), maxRob(nums[1:])) if len(nums) > 1 else nums[0]