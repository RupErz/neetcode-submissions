import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p1, p2):
            x1, y1 = p1 
            x2, y2 = p2
            return (math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))
        
        cur = []
        for p in points:
            dist = distance(p, [0, 0])
            cur.append((dist, p))
        
        heapq.heapify(cur)
        result = []

        print(cur)
        
        for i in range(k):
            result.append(cur[0][1])
            heapq.heappop(cur)
        
        return result