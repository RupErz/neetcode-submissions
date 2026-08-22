class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # DFS 
        # Build adjacency list
        adj = {}
        for s, d, amt in flights:
            if s not in adj:
                adj[s] = []
            adj[s].append((d, amt))
        
        memo = {}
        def dfs(cur, k):
            if cur == dst:
                return 0
            
            if cur not in adj:
                return float("inf")

            if k < 0:
                return float("inf")

            if cur in memo:
                return memo[(cur, k)]
            
            result = float("inf")

            for nei, amount in adj[cur]:
                price = dfs(nei, k - 1)

                if price != float("inf"):
                    result = min(result, amount + price)

            memo[(cur, k)] = result
            return result
        
        ans = dfs(src, k)
        return ans if ans != float("inf") else -1

                       

