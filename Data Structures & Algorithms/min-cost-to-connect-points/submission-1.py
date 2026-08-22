class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for x, y in points:
            adj[(x, y)] = []
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                # manhattan_distance = abs(x1 - x2) + abs(y1 - y2)
                adj[(x1, y1)].append((x2, y2))
                adj[(x2, y2)].append((x1, y1))
        
         
        minHeap = []
        firstX, firstY = points[0][0], points[0][1]

        for x2, y2 in adj[(firstX, firstY)]:
            manhattan_distance = abs(firstX - x2) + abs(firstY - y2)
            heapq.heappush(minHeap, (manhattan_distance, firstX, firstY, x2, y2))
        
        visit = set()
        visit.add((firstX, firstY))

        cost = 0

        while minHeap:
            distance, srcX, srcY, dstX, dstY = heapq.heappop(minHeap)
            if (dstX, dstY) in visit:
                continue
            
            visit.add((dstX, dstY))
            cost += distance

            for x2, y2 in adj[(dstX, dstY)]:
                if (x2, y2) not in visit:
                    manhattan_distance = abs(dstX - x2) + abs(dstY - y2)
                    heapq.heappush(minHeap, (manhattan_distance, dstX, dstY, x2, y2))
        
        return cost
