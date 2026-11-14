class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        def dfs(cur, curList):
            if cur >= len(nums):
                result.append(curList.copy())
                return
            
            curList.append(nums[cur])
            dfs(cur + 1, curList)
            curList.pop()

            while cur + 1 < len(nums) and nums[cur + 1] == nums[cur]:
                cur += 1
            dfs(cur + 1, curList)
        
        dfs(0, [])
        return result 
