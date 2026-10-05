class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, t in times:
            adj[s].append((d, t))
        
        minHeap = [(0, k)]
        visited = set()
        distance = {}
        heapq.heapify(minHeap)

        while minHeap:
            dist, dest = heapq.heappop(minHeap)
            if dest in visited:
                continue
            
            visited.add(dest)
            distance[dest] = dist
            for nei, cost in adj[dest]:
                heapq.heappush(minHeap, (dist + cost, nei))
        
        return max(distance.values()) if len(distance) == n else -1
            
