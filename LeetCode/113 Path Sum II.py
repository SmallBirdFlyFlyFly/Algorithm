# -*- coding: utf-8 -*-

'''
Path Sum II
===========

Given a binary tree and a sum, find all root-to-leaf paths where each path's
sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

return

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

import itertools


class Solution(object):
    '''算法思路：

    递归遍历即可
    '''
    def pathSum(self, root, sum):
        if not root:
            return []

        if not (root.left or root.right) and sum == root.val:
            return [[root.val]]

        return [[root.val] + p for p in itertools.chain(
                *[self.pathSum(c, sum - root.val) for c in (
                    root.left, root.right)])]


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'TreeNode {}'.format(self.val)


a = TreeNode(2)
b = TreeNode(5)

a.left = b

s = Solution()
print s.pathSum(a, 7)
