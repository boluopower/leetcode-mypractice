# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-5-27 23:58'

'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''


class Solution:
    """
    Time: O()
    Space:O()
    """

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums2) & set(nums1))
