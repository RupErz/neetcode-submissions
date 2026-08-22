class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) # built in function
        # but it basically a hash map
        maxHeap = [ -cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        # Everytime we pop from heap, we process it, time + 1
        while maxHeap or q: # We keep popping q when time matched
            time += 1
            if maxHeap:
                updVal = 1 + heapq.heappop(maxHeap)
                if updVal : # not 0
                    q.append([updVal, time + n])
            if q and q[0][1] == time :
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
        # Time : O (N)


