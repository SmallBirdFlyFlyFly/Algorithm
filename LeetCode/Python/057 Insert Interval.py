# -*- coding: utf-8 -*-

'''
Insert Interval
===============

Given a set of non-overlapping intervals, insert a new interval into the
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their
start times.

Example 1:

Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as
[1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''


class Solution(object):
    '''算法思路：

    二分查找，然后根据不同的情况进行 merge 即可
    '''
    def find(self, intervals, target):
        low, high = 0, len(intervals) - 1
        while low <= high:
            mid = low + high >> 1
            if target > intervals[mid].end:
                low = mid + 1
            elif target < intervals[mid].start:
                high = mid - 1
            else:
                return True, mid
        return False, low

    def insert(self, intervals, newInterval):
        (isInStart, iStart), (isInEnd, iEnd) = [
            self.find(intervals, i)
            for i in (newInterval.start, newInterval.end)
        ]

        start = intervals[iStart].start if isInStart else newInterval.start
        end = intervals[iEnd].end if isInEnd else newInterval.end

        iEnd += isInEnd

        return intervals[:iStart] + [Interval(start, end)] + intervals[iEnd:]


class Solution(object):
    '''算法思路：

    同上，

    找到 newInterval.start 和 newInterval.end 应该在的位置，然后根据

    newInterval.start 和 intervals[start].start
    newInterval.end 和 intervals[end].start

    二者的关系来进行覆盖
    '''
    def search(self, intervals, target):
        low, high = 0, len(intervals) - 1
        while low <= high:
            mid = low + high >> 1
            if intervals[mid].end < target:
                low = mid + 1
            else:
                if mid == 0 or intervals[mid - 1].end < target:
                    return mid
                high = mid - 1
        return low

    def insert(self, intervals, newInterval):
        n, MAX = len(intervals), float('inf')

        start, end = [
            self.search(intervals, t)
            for t in (newInterval.start, newInterval.end)
        ]

        before, after = intervals[:start], intervals[end + 1:]

        newInterval.start = min(
            intervals[start].start if start < n else MAX, newInterval.start)

        if end < n:
            if newInterval.end < intervals[end].start:
                return before + [newInterval, intervals[end]] + after
            newInterval.end = intervals[end].end

        return before + [newInterval] + after


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '<Interval start={} end={}>'.format(self.start, self.end)


s = Solution()
print s.insert([Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)], Interval(4, 9))
print s.insert([Interval(1, 5), Interval(8, 10), Interval(13, 17), Interval(20, 25)], Interval(7, 19))
print s.insert([Interval(0, 7), Interval(8, 8), Interval(9, 11)], Interval(4, 13))
