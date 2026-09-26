"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
            
        intervals.sort(key= lambda x: x.start)

        start = sorted([i.start for i in intervals])
        stop = sorted([i.end for i in intervals])

        rooms = 1
        j = 0

        for i in range(1, len(start)):
            # Compare against end time of prev occupied room
            if start[i] < stop[j]:
                # Still occupied
                rooms += 1
            else:
                # The prev room has been fred 
                # then no need to add room for this turn
                j += 1 # move this to next room been occupied
        
        return rooms 

        
            
        # [0, 5, 15] room = 2
        # [10, 20, 40]

