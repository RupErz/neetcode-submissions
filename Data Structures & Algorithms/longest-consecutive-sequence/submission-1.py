class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sort the array first
        if not nums:
            return 0 
        nums = sorted(nums)
        res = 1
        current = 0
        after = current + 1
        current_length = 1
        while current < (len(nums) - 1):
            if nums[after] - nums[current] == 1:
                current_length += 1
            elif nums[after] - nums[current] > 1:
                current_length = 1
            current = after
            after += 1
            res = max(res, current_length)
        return res