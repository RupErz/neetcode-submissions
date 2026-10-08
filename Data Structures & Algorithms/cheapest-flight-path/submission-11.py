class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Dijkstra wont work because it prio shortest path 
        # Prims not work because we already have the edge 
        # minHeap not work here because it always pop the lowest 
        # leave only 1 way DFS unless there is another algorithm support this 

        adj = defaultdict(list)


        for s, d, c in flights:
            adj[s].append((d, c))
        
        
        memo = {}
        result = float("inf")
        def dfs(cur, price, stops):
            nonlocal result
            if (cur, stops) in memo and memo[(cur, stops)] <= price:
                return
            if stops > k:
                return
            
            memo[(cur, stops)] = price
            for nei, cost in adj[cur]:
                if nei == dst:
                    result = min(result, price + cost)
                else:
                    dfs(nei, price + cost, stops + 1)
            
        dfs(src, 0, 0)
        return result if result != float("inf") else -1
            
