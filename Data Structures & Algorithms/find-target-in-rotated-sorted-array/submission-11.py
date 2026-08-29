class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            

            # Notice how we have 1 full sorted + 1 half sorted
            if nums[mid] >= nums[l]:
                # Left is the sorted
                # Use the bounds to check if target is inside
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                # Right is the sorted
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            
        return -1