class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Using 3 ptrs i,j,k
        if len(nums) >= 3:
            nums.sort()
 

        sol = []
        #We made use of 2 sum lessons, skip whenever our first pointer dup
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1] :
                continue
            j,k = i + 1, len(nums) - 1
            while j < k:
                threeSum = v + nums[j] + nums[k]
                if threeSum > 0 :
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    sol.append([v, nums[j], nums[k]])
                    j += 1 #Only update 1 ptr at a time -> left
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return sol
        #Time O(nlogn) + O(n^2)
