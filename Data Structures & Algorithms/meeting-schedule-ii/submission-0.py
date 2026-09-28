"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_r, min_heap = 0, []
        intervals.sort(key=lambda x:x.start)
        for inv in intervals:
            if min_heap and min_heap[0] <= inv.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,inv.end)
            max_r = max(max_r,len(min_heap))
        return max_r

        