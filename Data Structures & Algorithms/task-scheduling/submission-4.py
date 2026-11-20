from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
            # 2 heap  
            # 1 heap process
            # 1 heap cooldown (cur time + n, remaining)

            curTask = [] # max heap (amt, task)
            freq = Counter(tasks)
            for task, amt in freq.items():
                curTask.append((-amt, task))
            heapq.heapify(curTask)

            if len(tasks) == 1:
                return 1

            cooldown = [] # min heap for cooldown management (time, amt, task)
            time = 0


            while curTask or cooldown:
                if cooldown and time > cooldown[0][0]:
                    resumeTask = heapq.heappop(cooldown)
                    resumeTaskAmt, resumeTaskName = resumeTask[1], resumeTask[2]
                    heapq.heappush(curTask, (-resumeTaskAmt, resumeTaskName))
                
                # Pop the most freq one and start processing
                if curTask:
                    today = heapq.heappop(curTask)
                    todayLeft, todayTask = today

                    if abs(todayLeft) - 1 > 0:
                        heapq.heappush(cooldown, (time + n, -todayLeft - 1, todayTask))

                time += 1    

            return time                
        