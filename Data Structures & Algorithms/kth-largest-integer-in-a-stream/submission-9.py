class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums) 
        self.minHeap = nums 
        self.ith = k

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) 

             

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.ith:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        
