class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        leftmost, rightmost = -1, -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                leftmost = mid
            
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        
        lr, rr = 0, len(nums) - 1
        while lr <= rr:
            mid = (lr + rr) // 2

            if nums[mid] == target:
                rightmost = mid

            if nums[mid] > target:
                rr = mid - 1
            else:
                lr = mid + 1

        return [leftmost,  rightmost] 
            

