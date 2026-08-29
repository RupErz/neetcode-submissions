class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Find the largest

        # l, mid, r = 
        # check left , if > left = answer
        # check left , if < left = increasing (either at the first val or right side)
        # use l,mid,r to eliminate 

        l, r = 0, len(nums) - 1
        mid = (l + r) // 2
        shortest = nums[mid]

        while l <= r:

            mid = (l + r) // 2
            if nums[mid] > nums[l]:
                if nums[l] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                shortest = min(shortest, nums[mid])
                l += 1

        return shortest

                

