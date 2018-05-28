# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-5-28 23:13'

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        freq = defaultdict(int)
        for elem in nums:
            freq[elem] += 1
        if 0 in freq and freq[0] > 2:
            res = [[0, 0, 0]]
        else:
            res = []
        neg = sorted((filter(lambda x: x < 0, freq)))
        nneg = sorted((filter(lambda x: x >= 0, freq)))
        for elem1 in neg:
            for elem2 in nneg:
                src = -(elem1 + elem2)
                if src in freq:
                    if src in (elem1, elem2) and freq[src] > 1:
                        res.append([elem1, src, elem2])
                    elif src < elem1:
                        res.append([elem1, src, elem2])
                    elif src > elem2:
                        res.append([elem1, src, elem2])
        return res


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
