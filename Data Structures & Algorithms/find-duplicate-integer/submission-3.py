class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # l, h = 1, len(nums) - 1

        # while l < h:
        #     mid = (l + h) // 2

        #     # Check for any <= mid
        #     counter = 0
        #     for n in nums:
        #         if n <= mid:
        #             counter += 1
            
        #     if counter > mid:
        #         h = mid
        #     else:
        #         l = mid + 1

        # return l

        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
        return -1
