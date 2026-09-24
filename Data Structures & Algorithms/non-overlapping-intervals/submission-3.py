class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # First of all we have to sort them out to make sure overlap are adjacent and easy to manage
        intervals.sort() 

        # 1 2.  1 4   2 4
        # If we found an overlap then what to remove ? 
        # Since we alr sort based on the start, then the one with lower end will be kept the other is being removed 
        # But .sort() alr make sure that, so any latter on overlap can be removed 
        result = 0
        stack = []
        for i in range(len(intervals)):
            start, stop = intervals[i]
            if len(stack) == 0:
                stack.append([start, stop])
                continue
            
            # Since we alr sort we can jsut look back ONCE
            prevStart, prevStop = stack[-1]

            # Check for overlap 
            if prevStart < stop and prevStop > start:
                result += 1
                # Prioritize remove the larger end value
                if prevStop > stop:
                    stack.pop()
                    stack.append([start, stop])
            else:
                stack.append([start, stop]) 

        return result          




