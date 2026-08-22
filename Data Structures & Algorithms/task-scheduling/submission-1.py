class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Having a count start from 0 to count CPU cycles
        # using a maxHeap, to pop the most frequent task -> prevent idle
        # Using a queue to store as (# freq, count) whenever we process 

        count = 0
        # Finding the frequency and compress into maxHeap
        taskFreq = {}
        for i in range(len(tasks)) :
            taskFreq[tasks[i]] = 1 + taskFreq.get(tasks[i], 0)
        maxHeap = [ -i for i in taskFreq.values()]
        heapq.heapify(maxHeap)
        q = deque()

        while maxHeap or q :
            count += 1
            if maxHeap :
                # Process the task
                task = heapq.heappop(maxHeap) + 1 # since this is - numb , we + 1
                # if task is 0 then we dont do anything cause we done.
                if task != 0 :
                    q.append([count + n, task]) # Time , # freq
            if q and q[0][0] == count :
                # Pop them out and push back to our heap 
                updTask = q.popleft()[1]
                heapq.heappush(maxHeap, updTask)
        return count
