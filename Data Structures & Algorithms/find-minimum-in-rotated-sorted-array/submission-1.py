class Solution:
    def findMin(self, nums: List[int]) -> int:
        #When rotated, most of the time , there will be 2 sorted array
        # [3,4,5 , 1,2] , the left array always greater than right array 
        l, r = 0, len(nums) - 1
        res = nums[0]
         
        while l <= r :
            #1 case , if initially val of l < val of r : means its org list
            if nums[l] < nums[r]:
                return min(res, nums[l])
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] < nums[l] :
            # Which means mid is on the second sorted array
            # We want to find min , then we should move to the left since
            # right is greater than vd: [3,4,<-1->,2]
                r = m - 1 
            else:
                l = m + 1
        return res