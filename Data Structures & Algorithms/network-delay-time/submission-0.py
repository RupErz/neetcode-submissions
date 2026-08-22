class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for u, v, t in times:
            adj[u].append((v, t))
        
        shortest = {}
        minHeap = [(0, k)]
        heapq.heapify(minHeap)

        while minHeap:
            t1, dst = heapq.heappop(minHeap)
            if dst in shortest:
                continue
            shortest[dst] = t1

            for nei, t2 in adj[dst]:
                if nei not in shortest:
                    heapq.heappush(minHeap, (t1 + t2, nei))

        if len(shortest) != n:
            return -1
        result = 0
        for key, value in shortest.items():
            result = max(result, value)
        return result