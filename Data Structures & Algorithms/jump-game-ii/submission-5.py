class Solution:
    def jump(self, nums: List[int]) -> int:
        # Treat like a BFS, level by level
        # At each level we only pick the maximum furthest to go so technically it was each level = 1 jump
        furthest = 0
        maximum = 0
        count = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])
            if i == maximum:
                maximum = furthest
                count += 1
        return count

        
