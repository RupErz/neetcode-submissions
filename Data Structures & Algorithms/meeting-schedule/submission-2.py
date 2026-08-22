"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 5 10 15 20 0 30
        if len(intervals) == 0:
            return True

        intervals.sort(key=lambda x: (x.end)) # Sort based on the end val
        prevEnd = intervals[0].end

        for obj in intervals[1:]:
            start, end = obj.start, obj.end
            if prevEnd > start:
                return False
            prevEnd = end #Update prevEnd
        
        return True



