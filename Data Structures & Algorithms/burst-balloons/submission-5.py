class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        pad = [1] + nums + [1]
        memo = {}
        # 1 2 3 1
        def dfs(l, r):
            if r - l < 2:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            
            result = 0
            for i in range(l + 1, r):
                coins = pad[l] * pad[i] * pad[r]
                result = max(result, dfs(l, i) + coins + dfs(i, r))
            
            memo[(l, r)] = result
            return result

        return dfs(0, len(pad) - 1)