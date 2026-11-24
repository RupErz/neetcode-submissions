class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, h = 1, len(nums) - 1

        while l < h:
            mid = (l + h) // 2

            # Check for any <= mid
            counter = 0
            for n in nums:
                if n <= mid:
                    counter += 1
            
            if counter > mid:
                h = mid
            else:
                l = mid + 1

        return l
