class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []

        for u, v, w in edges:
            adj[u].append((v, w))
        
        shortest = {}
        minHeap = [(0, src)]
        heapq.heapify(minHeap)

        while minHeap:
            w1, s = heapq.heappop(minHeap)
            if s in shortest:
                continue
            shortest[s] = w1

            # Greedy BFS
            for dst, w2 in adj[s]:
                if dst not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, dst))
        if len(shortest) != n:
            for i in range(n):
                if i not in shortest:
                    shortest[i] = -1
        return shortest
        
            