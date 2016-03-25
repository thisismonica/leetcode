__author__ = 'monica_wang'

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        '''
        [[0, 14], [5, 16], [15,20]]
        rooms: 0([0,14])
        rooms: 2(0,14, 15,20), 1(5,16)
        '''
        if intervals == []:
            return 0

        intervals.sort(key=lambda x: x.start)

        # end time of meetings in each meeting room
        endTime = [intervals[0].end]
        heapq.heapify(endTime)


        # foreach new meeting, try to fit into meeting room with earliest end time
        for i in range(1, len(intervals)):
            if intervals[i].start < heapq.nsmallest(1,endTime)[0]:
                heapq.heappush(endTime, intervals[i].end)
            else:
                heapq.heappushpop(endTime, intervals[i].end)
        return len(endTime)
