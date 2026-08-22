class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(index, arr, curSum):
            if curSum > target or index == len(nums):
                return
            if curSum == target:
                result.append(arr.copy())
                return
            
            curSum += nums[index]
            arr.append(nums[index])
            backtrack(index, arr, curSum)

            curSum -= nums[index]
            arr.pop()
            backtrack(index + 1, arr,curSum)
        backtrack(0, [], 0)
        return result