class Solution:
    def canJump(self, nums: List[int]) -> bool:
        DESTINATION = len(nums) - 1
        for i in range(DESTINATION, -1, -1):
            if i + nums[i] >= DESTINATION:
                DESTINATION = i
        return True if DESTINATION == 0 else False
