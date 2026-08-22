class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Min heap , pop the min K times
        minHeap = []
        for x, y in points :
            distance = (x)**2 + (y)**2
            minHeap.append([distance, x , y])

        # For min heap, sorting key by defaut is the first
        # element in the list 
        # [ [1,2], [3,4] ] => 1 , 3 is sorting key 
        heapq.heapify(minHeap)
        res = []
        while k > 0 :
            res.append(heapq.heappop(minHeap)[1:])
            # How do we deal with duplicate ?
            k -= 1
        return res

