class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        
        for i in range(n):
            adj[i] = []
        for src, dst, w in edges:
            adj[src].append((dst, w))
            adj[dst].append((src, w))
        
        minHeap = []
        # Starting with node 0 (any)
        for node, w in adj[0]:
            heapq.heappush(minHeap, (w, 0, node))
        
        mst = 0
        visit = set()
        visit.add(0)

        while minHeap:
            w, src, dst = heapq.heappop(minHeap)
            if dst in visit:
                continue
            
            visit.add(dst)
            # mst.append([src, dst])
            mst += w
            for nei, w in adj[dst]:
                if nei not in visit:
                    heapq.heappush(minHeap, (w, dst, nei))
        if len(visit) != n:
            return -1
        return mst        