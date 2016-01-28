# -*- coding: utf-8 -*-

'''
Search Insert Position
======================

Given a sorted array and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''


class Solution(object):
    '''算法思路：

    二分查找
    '''
    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if nums[mid] < target:
                low = mid + 1
            else:
                if mid > 0 and nums[mid - 1] < target or mid == 0:
                    return mid
                high = mid - 1
        return low


s = Solution()
print s.searchInsert([1, 3], 4)
