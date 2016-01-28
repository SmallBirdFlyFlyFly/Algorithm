# -*- coding: utf-8 -*-

'''
Minimum Size Subarray Sum
=========================

Given an array of n positive integers and a positive integer s, find the
minimal length of a subarray of which the sum ≥ s. If there isn't one, return
0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

More practice:
If you have figured out the O(n) solution, try coding another solution of which
the time complexity is O(n log n).
'''


class Solution(object):
    '''算法思路：

    双指针，sliding window, 整个运动轨迹呈 虫爬行 状

    head 一直往前探索直到 [tail, head) 子串和不小于 s，然后再把
    tail 往前探索一直到子串和小于 s，期间比较子串的长度

    Time: O(n)
    '''
    def minSubArrayLen(self, s, nums):
        head, tail, n, minimal, collect = 0, 0, len(nums), float('inf'), 0
        while 1:
            while head < n and collect < s:
                collect += nums[head]
                head += 1

            if head >= n and collect < s:
                break

            while tail < head and collect >= s:
                minimal = min(minimal, head - tail)
                collect -= nums[tail]
                tail += 1

        return 0 if minimal == float('inf') else minimal


class Solution(object):
    '''算法思路：

    看到 log(n) 就应该想到二分查找，二分查找需要数组是有序的，而 nums 不是有序的，
    但是看到数组里的元素是有序的，则其前 n 项和必定是递增的，对于每一个元素，找到其后边
    不小于 s 的 index 最小的元素，比较子串的长度即可

    Time: O(n*log(n))
    '''
    def search(self, sums, start, s):
        low, high = start, len(sums) - 1
        while low <= high:
            mid = low + high >> 1
            if sums[mid] < s:
                low = mid + 1
            else:
                if mid > 0 and sums[mid - 1] < s or mid == 0:
                    return mid
                high = mid - 1
        return float('inf')

    def minSubArrayLen(self, s, nums):
        sums = []
        for i, num in enumerate(nums):
            sums.append((sums[i - 1] if i > 0 else 0) + num)

        minimal = float('inf')
        for i, num in enumerate(nums):
            end = self.search(sums, i, s + (sums[i - 1] if i > 0 else 0))
            minimal = min(minimal, end - i + 1)

        return 0 if minimal == float('inf') else minimal


s = Solution()
print s.minSubArrayLen(10, [])
print s.minSubArrayLen(697439, [5334,6299,4199,9663,8945,3566,9509,3124,6026,6250,7475,5420,9201,9501,38,5897,4411,6638,9845,161,9563,8854,3731,5564,5331,4294,3275,1972,1521,2377,3701,6462,6778,187,9778,758,550,7510,6225,8691,3666,4622,9722,8011,7247,575,5431,4777,4032,8682,5888,8047,3562,9462,6501,7855,505,4675,6973,493,1374,3227,1244,7364,2298,3244,8627,5102,6375,8653,1820,3857,7195,7830,4461,7821,5037,2918,4279,2791,1500,9858,6915,5156,970,1471,5296,1688,578,7266,4182,1430,4985,5730,7941,3880,607,8776,1348,2974,1094,6733,5177,4975,5421,8190,8255,9112,8651,2797,335,8677,3754,893,1818,8479,5875,1695,8295,7993,7037,8546,7906,4102,7279,1407,2462,4425,2148,2925,3903,5447,5893,3534,3663,8307,8679,8474,1202,3474,2961,1149,7451,4279,7875,5692,6186,8109,7763,7798,2250,2969,7974,9781,7741,4914,5446,1861,8914,2544,5683,8952,6745,4870,1848,7887,6448,7873,128,3281,794,1965,7036,8094,1211,9450,6981,4244,2418,8610,8681,2402,2904,7712,3252,5029,3004,5526,6965,8866,2764,600,631,9075,2631,3411,2737,2328,652,494,6556,9391,4517,8934,8892,4561,9331,1386,4636,9627,5435,9272,110,413,9706,5470,5008,1706,7045,9648,7505,6968,7509,3120,7869,6776,6434,7994,5441,288,492,1617,3274,7019,5575,6664,6056,7069,1996,9581,3103,9266,2554,7471,4251,4320,4749,649,2617,3018,4332,415,2243,1924,69,5902,3602,2925,6542,345,4657,9034,8977,6799,8397,1187,3678,4921,6518,851,6941,6920,259,4503,2637,7438,3893,5042,8552,6661,5043,9555,9095,4123,142,1446,8047,6234,1199,8848,5656,1910,3430,2843,8043,9156,7838,2332,9634,2410,2958,3431,4270,1420,4227,7712,6648,1607,1575,3741,1493,7770,3018,5398,6215,8601,6244,7551,2587,2254,3607,1147,5184,9173,8680,8610,1597,1763,7914,3441,7006,1318,7044,7267,8206,9684,4814,9748,4497,2239])
