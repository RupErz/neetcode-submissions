class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # red, blue, green
        # at the first house it can be colored either RBG
        # each decision will have a result => must try out all
        # DFS might be a good choice
        # First house can have 3 choices, the latter only 2 choices
    
        # Time: O()

        memo = {}
        def dfs(i, color):
            if i == len(costs):
                return 0
            
            if (i, color) in memo:
                return memo[(i, color)]

            total = float("inf")

            # Tracing through 3 colors
            for c in range(3):
                if color != c:
                    amount = costs[i][color] + dfs(i + 1, c)
                    total = min(total, amount)
            
            memo[(i, color)] = total
            return total


        result = float("inf")

        for c in range(3):
            total = dfs(0, c)
            result = min(result, total)

        
        return result

