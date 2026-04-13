"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        count = 0
        hp = []


        for iv in intervals:
            if hp and hp[0] <= iv.start:
                heapq.heappop(hp)
            
            heapq.heappush(hp, iv.end)
        
        return len(hp)
        