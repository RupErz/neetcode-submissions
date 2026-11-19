class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            first, second = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            
            if first == second:
                continue
            
            if first > second:
                heapq.heappush(maxHeap, -first + second)
            else:
                heapq.heappush(maxHeap, -second + first)
        
        return -maxHeap[0] if len(maxHeap) > 0 else 0