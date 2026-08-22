class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)

        # We need to keep poping until our heap reach its K element:
        # Min heap pop = pop the min val from it, allow to have the rest
        # as largest nth element
        while len(self.heap) > self.k : 
            heapq.heappop(self.heap)
            # Make it become Min Heap Size K.

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # What if the initial list is not big enough for Kth
        # We only pop to maintain min heap size K if our heap is enough size.
        if len(self.heap) > self.k :
            heapq.heappop(self.heap)
        return self.heap[0]

        
