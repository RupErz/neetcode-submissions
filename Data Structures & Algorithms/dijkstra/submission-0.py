class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Create a dictionary with list as DEFAULT value
        adj = defaultdict(list)

        # Map the edges 
        # Source : [ (destination, weight) ]
        for s, d, w in edges:
            adj[s].append((d, w))

        shortest = {}
        # Create a min heap
        # ( weight, destination )
        # By default from source to src is weight 0
        pending = [(0, src)]

        while pending:
            # Pop from heap = guarantee shortest distance
            w, d = heapq.heappop(pending)

            # Check if we already have it in our map or now
            if d in shortest:
                continue
            shortest[d] = w

            # BFS : Visit all neighbor and give an estimated value
            for nd, nw in adj[d]:
                # Only visit if we not found its shortest path yet
                if nd not in shortest:
                    heapq.heappush(pending, (w + nw, nd))
        # Mark all unreached vertices as -1
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1 
        return shortest
