class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Can we do maxHeap
        maxHeap = []
        for x, y in points :
            distance = (x)**2 + (y)**2 
            maxHeap.append([-distance, x, y])
        heapq.heapify(maxHeap)

        while len(maxHeap) > k :
            heapq.heappop(maxHeap)
        res = [ i[1:] for i in maxHeap ]
        return res
        
