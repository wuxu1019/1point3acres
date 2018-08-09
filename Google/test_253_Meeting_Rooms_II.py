"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms_bruteforce(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        ct = collections.Counter()

        for i in intervals:
            for i in range(i.start, i.end):
                ct[i] += 1
        return max(ct.values())

    def minMeetingRooms_heap(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda v:v.start)

        heap = []

        for i in intervals:
            if heap and i.start >= heap[0]:
                heapq.heapreplace(heap, i.end)
            else:
                heapq.heappush(heap, i.end)
        return len(heap)

    def minMeetingRooms_count_tricky(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        s, e = [], []
        for i in intervals:
            s.append(i.start)
            e.append(i.end)
        s.sort()
        e.sort()
        available, rooms = 0, 0
        i, j = 0, 0
        while i < len(s):
            if s[i] < e[j]:
                if available:
                    available -= 1
                else:
                    rooms += 1
                i += 1
            else:
                j += 1
                available += 1
        return rooms

