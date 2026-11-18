class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        for i in range(k - 1):
            heapq.heappop(maxHeap)
        
        return -maxHeap[0]