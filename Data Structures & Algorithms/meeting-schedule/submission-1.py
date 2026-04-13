"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        for i in range(len(intervals)):
            if i > 0:
                x1,y1 = intervals[i-1].start, intervals[i-1].end
                x2,y2 = intervals[i].start, intervals[i].end

                if y1 > x2: return False
        
        return True



