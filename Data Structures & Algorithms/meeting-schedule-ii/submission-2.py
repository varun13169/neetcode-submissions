"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from queue import PriorityQueue

class Solution:
    def getSortKey(self, t):
        return t.start

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals.sort(key=lambda x: x[0])
        intervals.sort(key=self.getSortKey)
        pq = PriorityQueue()

        for interval in intervals:
            # print(pq.qsize())
            if pq.qsize() == 0:
                pq.put((interval.end, [interval.start, interval.end]))
            else:
                earliestRoomAvailable = pq.get()
                # print(earliestRoomAvailable, interval)
                if earliestRoomAvailable[1][1] > interval.start:
                    pq.put((earliestRoomAvailable[1][1], earliestRoomAvailable[1]))
                pq.put((interval.end, [interval.start, interval.end]))
            # print(pq.qsize())

        

        return pq.qsize()
