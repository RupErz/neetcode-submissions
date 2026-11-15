class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(cur, curList):
            if cur >= len(nums):
                result.append(curList.copy())
                return
            
            curList.append(nums[cur])
            dfs(cur + 1, curList)
            curList.pop()

            dfs(cur + 1, curList)

        dfs(0, [])
        return result 
