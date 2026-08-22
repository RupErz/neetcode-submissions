class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [ -i for i in stones ]
        heapq.heapify(self.maxHeap)

        while len(self.maxHeap) >= 2 :
            maxF = -heapq.heappop(self.maxHeap)
            maxS = -heapq.heappop(self.maxHeap)

            if maxF != maxS :
                newVal = maxF - maxS if  maxF > maxS else maxS - maxF
                heapq.heappush(self.maxHeap, -newVal)
        return -self.maxHeap[0] if len(self.maxHeap) != 0 else 0    
