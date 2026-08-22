class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Greedy: prio the most task #
        freq = Counter(tasks) 
        cooldown = {}
        timer = 0
        
        # Initially set cd to 0
        cooldown = deque()

        # Convert into max heap
        available = [(-val, key) for key, val in freq.items()]
        heapq.heapify(available)

        while available or cooldown:
            timer += 1

            if cooldown and timer >= cooldown[-1][0]:
                cd, val, key = cooldown.pop()
                heapq.heappush(available, (val, key))

            if available:
                # Find the max freq
                targetVal, targetKey = heapq.heappop(available)

                # Do the task
                if targetVal + 1 != 0:
                    cooldown.appendleft((timer + n + 1, targetVal + 1, targetKey))
                # When to pop them out ? Before we pop ?

        return timer


    
        