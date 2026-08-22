class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Decide target belong to first or second array 
        l, r = 0, len(nums) - 1
        while l <= r :
            m = (l + r) // 2
            if nums[m] == target :
                return m
            
            if nums[m] >= nums[l]:
                if nums[m] > target :
                    if target >= nums[l]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    l = m + 1
            else:
                if nums[m] > target:
                    r = m - 1
                else:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
        return - 1

