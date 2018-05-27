# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-5-28 0:18'

'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
'''


class Solution:
    """
    Time: O()
    Space:O()
    """

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        freq = defaultdict(int)
        for i in nums1:
            freq[i] += 1
        res = []
        for i in nums2:
            if freq[i] > 0:
                res.append(i)
                freq[i] -= 1
        return res

        # 别人的实现
        # if len(s) != len(t):
        #     return False
        # if s == t:
        #     return True
        # for i in map(chr, range(97, 123)):
        #     if s.count(i) != t.count(i):
        #         return False
        # return True
