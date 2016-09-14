# -*- coding: utf-8 -*-

'''
Jump Game II
============

Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from
index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
'''


class Solution(object):
    '''算法思路：

    DP

    结果：TLE
    '''
    def jump(self, nums):
        n = len(nums)
        steps = [0] * n

        for i in xrange(n - 2, -1, -1):
            steps[i] = min([
                1 + steps[min(i + step, n - 1)]
                for step in xrange(1, nums[i] + 1)
            ] or [float("inf")])

        return steps[0]


class Solution(object):
    '''算法思路：

    惰性，当之前的 maxReach 不足以支撑到现在位置的时候切换 reach，而不是一有比现在
    maxReach 大的时候就切换，注意切换时机
    '''
    def jump(self, nums):
        r, reach, maxReach = 0, 0, 0
        for i in xrange(len(nums)):
            if reach < i:
                reach = maxReach
                r += 1
            maxReach = max(maxReach, i + nums[i])
        return r


s = Solution()
print s.jump([1, 2, 3])
