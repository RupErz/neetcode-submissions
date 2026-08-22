class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for src, dst in tickets: 
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)
        
        for key in adj:
            adj[key].sort() # Sort the dst in lexico order
            adj[key] = deque(adj[key])
        
        result = []
        def dfs(src):
            # While src exist and have neighbor to travel
            while src in adj and adj[src]:
                next_dest = (adj[src]).popleft() # O(N)
                dfs(next_dest)
            result.append(src)

        dfs("JFK")
        return result[::-1]
