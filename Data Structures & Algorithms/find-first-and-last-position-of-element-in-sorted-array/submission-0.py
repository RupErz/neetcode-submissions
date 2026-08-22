class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                l, r = mid, mid
                break
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        if l > r:
            return [-1, -1]
        
        while l - 1 >= 0 and nums[l - 1] == nums[l]:
            l -= 1
        
        while r + 1 < len(nums) and nums[r + 1] == nums[r]:
            r += 1
        
        return [l, r]
            

