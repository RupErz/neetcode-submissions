class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford (optimal)
        # Imagine with k we can explore k levels

        # Bellman Ford: Find the shortest path within a constraints ~ dijkstra
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices.copy()

            for source, destination, cost in flights:
                if prices[source] != float("inf"):
                    amount = prices[source] + cost
                    temp[destination] = min(temp[destination], amount)
            prices = temp

        return prices[dst] if prices[dst] != float("inf") else -1


        
        # DFS 
        # Build adjacency list
        # adj = {}
        # for s, d, amt in flights:
        #     if s not in adj:
        #         adj[s] = []
        #     adj[s].append((d, amt))
        
        # memo = {}
        # def dfs(cur, k):
        #     if cur == dst:
        #         return 0
            
        #     if cur not in adj:
        #         return float("inf")

        #     if k < 0:
        #         return float("inf")

        #     if cur in memo:
        #         return memo[(cur, k)]
            
        #     result = float("inf")

        #     for nei, amount in adj[cur]:
        #         price = dfs(nei, k - 1)

        #         if price != float("inf"):
        #             result = min(result, amount + price)

        #     memo[(cur, k)] = result
        #     return result
        
        # ans = dfs(src, k)
        # return ans if ans != float("inf") else -1

                       

