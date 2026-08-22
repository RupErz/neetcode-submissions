class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # # Brute force : 
        # Going thru each element and check both neighbor
        # End up in O(n)

        # # Sort it : [1, 1, 2, 3] => 3 is the greatest. 
        # Find the index of number 3 within the org array => O(n)

        # Binary Search O(logN)
        # Start at middle, look for 2 neighbors
        # if nei > : uphill , so next is likely a peak
        # if nei < : downhill, so next is not likely a peak
        # if both nei > : prioritize anywhere
        # if both nei < : it is time to stop 
        left = 0
        right = len(nums) - 1
        while left <= right :
            mid = (left + right) // 2

            left_nei = nums[mid - 1] if mid - 1 >= 0 else float("-inf")
            right_nei = nums[mid + 1] if mid + 1 < len(nums) else float("-inf")

            if (left_nei < nums[mid] and right_nei < nums[mid]):
            # F -> 1 of them or both is greater
                return mid
            if (left_nei > nums[mid] and right_nei > nums[mid]) or (right_nei > nums[mid]):
                # Choose to go right
                left = mid + 1
            else :
                right = mid - 1
        
        

            

        