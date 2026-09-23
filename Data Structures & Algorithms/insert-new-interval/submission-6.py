class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Optimal : Time: O(N), Space: O(1)
        result = []
        startNew, endNew = newInterval
        added = False

        for start, end in intervals:
            if end < startNew:
                result.append([start, end])
            elif start <= endNew:
                startNew, endNew = min(start, startNew), max(end, endNew)
            else:
                if not added:
                    result.append([startNew, endNew])
                    added = True
                result.append([start, end])
        
        if not added:
            result.append([startNew, endNew])
        return result
        
    
        # -------------
        # sN           eN
 
        # Insert into the intervals
        # Time : O(N), Space: O(N)
        # startNew, endNew = newInterval
        # inserted = []

        # if not intervals:
        #     inserted.append([startNew, endNew])
        # else:
        #     for start, end in intervals:
        #         if startNew < start:
        #             inserted.append([startNew, endNew])
        #         inserted.append([start, end])
        
        # # Start merge
        # stack = []
        # stack.append(inserted[0])

        # for i in range(1, len(inserted)):
        #     startA, endA = inserted[i][0], inserted[i][1]
        #     startB, endB = stack[-1][0], stack[-1][1]

        #     if startA <= endB and endA >= startB:
        #         # Start merging
        #         stack.pop()
        #         stack.append([min(startA, startB), max(endA, endB)])
        #     else:
        #         stack.append([startA, endA])
        
        # return stack
