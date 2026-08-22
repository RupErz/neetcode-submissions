class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curSet = []
        result = []

        def helper(i, nums, curSet, result):
            if i >= len(nums):
                result.append(curSet.copy())
                return
            
            # Pick the number
            curSet.append(nums[i])
            helper(i + 1, nums, curSet, result)
            curSet.pop()

            # Skip the number
            while i + 1 in range(len(nums)) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, nums, curSet, result)
        
        helper(0, nums, curSet, result)
        return result