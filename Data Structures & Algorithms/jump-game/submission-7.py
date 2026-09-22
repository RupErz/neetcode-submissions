class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # visited = {}
        # def dfs(i):
        #     if i == len(nums) - 1:
        #         return True
        #     if i in visited:
        #         return visited[i]
        #     canJump = False
        #     for step in range(1, nums[i] + 1):
        #         if dfs(i + step):
        #             canJump = True
        #             break
        #     visited[i] = canJump
        #     return canJump 
        # return dfs(0)

        # Track furthese index we can reach as iterate over the nums
        furthest = 0
        for i in range(len(nums)):
            if i <= furthest:
                furthest = max(furthest, i + nums[i])
            if furthest >= len(nums) - 1:
                return True
        
        return False

