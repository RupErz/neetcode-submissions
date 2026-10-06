class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Start at any point, mark it visited
        # Push cost to reach all unvisited neighbors into min-heap
        # Pop the cheapest, add it to total cost, mark visited
        # Push that new point's connections to unvisited points
        # Repeat until all points visited

        visited = set()
        minHeap = [(0, points[0][0], points[0][1])] # x, y, total distance
        heapq.heapify(minHeap)
        total_cost = 0

        while minHeap and len(visited) != len(points):
            dist, x, y= heapq.heappop(minHeap)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            total_cost += dist

            for nx, ny in points:
                if (nx, ny) not in visited:
                    distance = abs(x - nx) + abs(y - ny)
                    heapq.heappush(minHeap, (distance, nx, ny))

        
        return total_cost
                