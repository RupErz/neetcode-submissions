class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Min Heap : 
        minHeap = []
        for x, y in points:
            distance = (x)**2 + (y)**2
            minHeap.append([distance, x, y])
        heapq.heapify(minHeap)

        res = []
        while k > 0 :
            res.append(heapq.heappop(minHeap)[1:])
            k -= 1
        return res

