class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1: 1, 2: 2, 3: 3
        # most freq 

        # min heap ? 
        # pop until theres only 2 
        
        # or max heap 
        # pop exactly k times

        # (freq, value)
        counter = {}
        for n in nums: 
            if n not in counter:
                counter[n] = 0
            counter[n] += 1

        heap = []
        for key, val in counter.items():
            heap.append((val, key))
        # Build the heap
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        result = []
        for freq, num in heap:
            result.append(num)
        
        return result

# 0: 2
# 1: 1
# 3: 1