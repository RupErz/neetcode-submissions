class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 1: [0 , 2]
        # 0: [2]

        # start = 1 
        # end = 2
        # k = 1 ( 0 or 1 )

        # 1 -> 0 -> 2: destination stop calcualte price
        # 1 -> 2 : destination 

        # Build adjacency list
        adj = {}
        for s, d, amt in flights:
            if s not in adj:
                adj[s] = []
            adj[s].append((d, amt))
        
        def dfs(cur, k):
            if cur == dst:
                return 0
            
            if cur not in adj:
                return float("inf")

            if k < 0:
                return float("inf")
            
            result = float("inf")

            for nei, amount in adj[cur]:
                price = dfs(nei, k - 1)

                if price != float("inf"):
                    result = min(result, amount + price)

            return result 
        
        ans = dfs(src, k)
        return ans if ans != float("inf") else -1

        # total + (1, 0, 200)
        # (1, 0, 200) 
        # [3, 2] - 500 result = 500
        # [2] 200 + 0

                       

