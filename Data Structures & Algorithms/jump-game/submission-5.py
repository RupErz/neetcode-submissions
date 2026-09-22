class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = {}
        def dfs(i):
            if i == len(nums) - 1:
                return True
            
            if i in visited:
                return visited[i]

            canJump = False

            for step in range(1, nums[i] + 1):
                if dfs(i + step):
                    canJump = True
                    break

            visited[i] = canJump
            return canJump 

        return dfs(0)