"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 5 10 15 20 7 35 0 40
        if len(intervals) == 0:
            return 0

        start = [obj.start for obj in intervals]
        end = [obj.end for obj in intervals]
        start.sort()
        end.sort()

        count, s, e = 0, 0, 0
        res = 0

        while s < len(start):
            curStart, curEnd = start[s], end[e]
            if curStart < curEnd:
                # 1 meeting has just started
                count += 1
                s += 1
            else:
                # 1 meeting about to stop
                count -= 1
                e += 1
            res = max(res, count)
        
        return res

        