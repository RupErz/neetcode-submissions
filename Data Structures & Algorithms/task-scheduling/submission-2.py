class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for i in range(len(tasks)) :
            freq[tasks[i]] = 1 + freq.get(tasks[i], 0)
        maxHeap = [ -i for i in freq.values() ]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while q or maxHeap :
            time += 1
            if maxHeap :
                remainTime =  heapq.heappop(maxHeap) + 1
                if remainTime != 0 :
                    q.append([ time + n, remainTime ]) 
            if q and q[0][0] == time:
                wake = q.popleft()[1]
                heapq.heappush(maxHeap, wake)
        return time