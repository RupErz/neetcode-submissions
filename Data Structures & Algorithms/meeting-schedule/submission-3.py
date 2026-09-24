"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        possible = True
        for i in range(1, len(intervals)):
            curStart, curStop = intervals[i].start, intervals[i].end
            prevStart, prevStop = intervals[i - 1].start, intervals[i - 1].end

            # Check for conflict
            if prevStart < curStop and prevStop > curStart:
                possible = False
                break

        return possible

