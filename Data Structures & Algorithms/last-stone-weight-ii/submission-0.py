class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2

        cache = {}
        def dfs(i, curSum):
            if i >= len(stones) or curSum >= target:
                left = curSum
                right = stoneSum - left
                return abs(left - right)
            if (i, curSum) in cache:
                return cache[(i, curSum)]

            cache[(i, curSum)] = min(dfs(i + 1, curSum), dfs(i + 1, curSum + stones[i]))

            return cache[(i, curSum)]
        return dfs(0, 0)