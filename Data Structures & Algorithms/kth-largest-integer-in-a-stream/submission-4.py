class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.target = k
        heapq.heapify(self.heap) # Turn it into a min heap
        while len(self.heap) > k :
            heapq.heappop(self.heap) # Pop the min value
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.target :
            heapq.heappop(self.heap)
        return self.heap[0]