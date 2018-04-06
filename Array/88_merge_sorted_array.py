# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-4-4 20:10'


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while j < n and i < len(nums1):
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
            i += 1
        if j < n:
            nums1[i:] = nums2[j:]
        print(nums1)


s = Solution()
s.merge([2, 4, 6], 3, [1, 2, 3, 5, 7], 5)
