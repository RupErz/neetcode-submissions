class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort based on the starting value 
        # [1, 2] [1, 4] [2, 4]
        intervals.sort()
        removal = 0
        temp = [intervals[0]]

        for i in range(1, len(intervals)):
            startA, endA = temp[-1][0], temp[-1][1]
            startB, endB = intervals[i][0], intervals[i][1]

            # If it's overlap ?
            if startA < endB and endA > startB:
                if endA > endB:
                    temp.pop()
                    temp.append([startB, endB])
                removal += 1
            else:
                temp.append([startB, endB])
        
        return removal

                

        

